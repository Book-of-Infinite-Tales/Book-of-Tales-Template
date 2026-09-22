#!/usr/bin/env python3
"""Check a book.json against the house style of the published Book of Tales.

Usage:
    python lint_tales.py path/to/book.json [--quiet]

Reports ERRORS (rules the style always keeps) and WARNINGS (likely drift), then
a summary of skill balance and story-token threads. Exit status is 1 when there
are errors. This complements, and does not replace, the reader's own validation.
"""
import json
import os
import re
import sys
from collections import Counter

SKILLS = {
    "Warfare": "Martial", "Sword & Shield": "Martial", "Mounted": "Martial",
    "Piety": "Spiritual", "Wisdom": "Spiritual", "Magic": "Spiritual",
    "Diplomacy": "Courtly", "Cunning": "Courtly", "Honor": "Courtly",
    "Nature Lore": "Wilderness", "Endure Hardship": "Wilderness", "Hunting": "Wilderness",
}
CATEGORIES = {"Martial", "Spiritual", "Courtly", "Wilderness"}
RENOWN = {"Divinity", "Romance", "Villainy", "Any"}
PLAYER_KNIGHTS = ["Lancelot", "Palomides", "Palamedes", "Gawain", "Galahad", "Percival", "Perceval", "Parsifal",
                  "Tristan", "Tristram", "Enid", "Bradamante"]
ARCHAIC = ["prithee", "thee", "thou", "thy", "thine", "hath", "doth", "'tis", "ye", "methinks",
           "forsooth", "verily", "hither", "whither", "betwixt", "naught", "mayhap", "wherefore", "art thou"]
MODERN = ["okay", "ok,", "deal with it", "stressful", "trauma", "closure", "boundaries", "awesome", "guys"]
PHYSICAL = "Refer to physical Book of Tales for this passage."

errors, warnings = [], []


def words(text):
    return len(re.findall(r"[A-Za-z']+", text or ""))


def err(eid, msg):
    errors.append(f"{eid}: {msg}")


def warn(eid, msg):
    warnings.append(f"{eid}: {msg}")


def load(path):
    with open(path) as f:
        book = json.load(f)
    entries = book["entries"]
    if isinstance(entries, str):
        with open(os.path.join(os.path.dirname(path), entries)) as f:
            entries = json.load(f)
    if isinstance(entries, dict):
        entries = [dict(v, id=v.get("id", k)) for k, v in entries.items()]
    return book, {e["id"]: e for e in entries}


def check_text(eid, text, where):
    for name in PLAYER_KNIGHTS:
        if re.search(r"\b" + name + r"\b", text):
            err(eid, f"{where} names {name}; leave the player characters out")
    low = text.lower()
    for m in MODERN:
        if re.search(r"\b" + re.escape(m), low):
            warn(eid, f"{where} uses modern idiom '{m.strip(',')}'")
    if text.count("—") > 3:
        warn(eid, f"{where} has {text.count(chr(0x2014))} em-dashes; prefer short sentences")


def check_rewards_skill(eid, using, failure):
    """A failed skill check should teach a skill."""
    r = (failure or {}).get("rewards") or {}
    if all(u in RENOWN for u in using):
        return  # renown checks need not grant a skill
    if not r.get("skills") and "Gain " not in (failure.get("body") or ""):
        warn(eid, f"failure on {using} gains no skill; failure should teach (usually the skill tested)")


def destiny_value(r):
    d = (r or {}).get("destiny")
    return d if isinstance(d, int) else None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    quiet = "--quiet" in sys.argv
    book, E = load(path)

    skill_use = Counter()
    awarded, checked = {}, {}
    total_words = 0
    archaic = Counter()

    for eid, e in E.items():
        body = e.get("body", "")
        if body.strip() == PHYSICAL:
            continue
        total_words += words(body)
        check_text(eid, body, "body")
        low = " " + body.lower() + " "
        for a in ARCHAIC:
            archaic[a] += len(re.findall(r"(?<![a-z'])" + re.escape(a) + r"(?![a-z])", low))
        for m in re.finditer(r"Story Token #(\d+)", body):
            checked.setdefault(int(m.group(1)), set()).add(eid)
        if (e.get("rewards") or {}).get("storyToken"):
            awarded.setdefault(e["rewards"]["storyToken"], set()).add(eid)
        if words(body) > 30 and not re.search(r"\byou(r)?\b", body, re.I):
            warn(eid, "body never addresses 'you'; write in the second person")

        responses = e.get("responses") or []
        is_gate = responses and all(r.get("label", "").startswith(("If ", "Otherwise")) for r in responses)
        if responses and not is_gate:
            n = words(body)
            if n < 50:
                warn(eid, f"response body is {n} words (typical 80–300)")
            elif n > 350:
                warn(eid, f"response body is {n} words (typical 80–300)")
            if len(responses) > 4:
                warn(eid, f"{len(responses)} choices; the book uses 2, sometimes 3")
            has_dialogue = re.search(r"[\"“‘]|(^|\s)'[A-Z]", body)
            if not has_dialogue and e.get("id", "").isdigit() and int(e["id"]) < 2200:
                warn(eid, "character-encounter response has no dialogue")
        for r in responses:
            label = r.get("label", "")
            check_text(eid, label, "choice")
            for m in re.finditer(r"Story Token #(\d+)", label):
                checked.setdefault(int(m.group(1)), set()).add(eid)
            core = label.lstrip("* ").strip()
            if not (core.startswith("You may") or core.startswith(("If ", "Otherwise"))):
                err(eid, f"choice '{label[:50]}' should start with 'You may'")
            if any(re.search(r"\buse " + re.escape(s) + r"\b", label) for s in SKILLS):
                err(eid, f"choice '{label[:50]}' names a skill; name the deed instead")
            if r.get("romantic") and not label.startswith("*"):
                warn(eid, f"romantic choice '{label[:40]}' should start with '* '")
            if label.startswith("*") and not r.get("romantic"):
                warn(eid, f"choice '{label[:40]}' starts with '*' but is not marked romantic")
            g = r.get("goto", "")
            if g.isdigit() and eid.isdigit() and abs(int(g) - int(eid)) <= 2:
                warn(eid, f"choice leads to {g}, right next to {eid}; scatter linked passages")

        res = e.get("resolutions") or []
        if len(res) > 2:
            warn(eid, f"{len(res)} check options; the book uses 1 or 2")
        for o in res:
            using = o.get("using", [])
            for u in using:
                if u in SKILLS:
                    skill_use[u] += 1
                elif u in CATEGORIES:
                    skill_use["(" + u + ")"] += 1
                elif u in RENOWN:
                    skill_use["[" + u + "]"] += 1
            if len(using) > 2:
                warn(eid, f"option uses {len(using)} skills; use one, a pair, or a category")
            t = o.get("target")
            if isinstance(t, int):
                if all(u in RENOWN for u in using):
                    if not 1 <= t <= 6:
                        warn(eid, f"renown threshold {t} is unusual (book uses 3–5)")
                elif not 2 <= t <= 8:
                    warn(eid, f"target {t} is outside the book's range (2–8; 4–5 standard)")
            elif isinstance(t, dict) and not 1 <= t.get("base", 0) <= 5:
                warn(eid, f"location target base {t.get('base')} is unusual (book uses 2–5, mostly 3)")
            s, f = o.get("success") or {}, o.get("failure") or {}
            for side, oc in (("success", s), ("failure", f)):
                check_text(eid, oc.get("body", ""), side)
                total_words += words(oc.get("body", ""))
                n = words(oc.get("body", ""))
                if n < 20:
                    warn(eid, f"{side} body is {n} words (typical 40–220)")
                elif n > 260:
                    warn(eid, f"{side} body is {n} words (typical 40–220)")
                tok = (oc.get("rewards") or {}).get("storyToken")
                if tok:
                    awarded.setdefault(tok, set()).add(eid)
                for m in re.finditer(r"Story Token #(\d+)", oc.get("body", "")):
                    checked.setdefault(int(m.group(1)), set()).add(eid)
            if not (s.get("rewards") or {}):
                warn(eid, "success grants nothing")
            check_rewards_skill(eid, using, f)
            ds, df = destiny_value(s.get("rewards")), destiny_value(f.get("rewards"))
            if ds is not None and df is not None and df >= ds:
                warn(eid, f"failure destiny ({df}) is not less than success destiny ({ds})")

    # story token threads
    for tok, where in sorted(awarded.items()):
        readers = checked.get(tok, set()) - where
        if not readers:
            warn(f"token {tok}", f"awarded at {', '.join(sorted(where))} but never checked")
    for tok, where in sorted(checked.items()):
        if tok not in awarded:
            warn(f"token {tok}", f"mentioned at {', '.join(sorted(where))} but never awarded")

    # archaism budget: about 1 per 1,000 words in the published book
    arch_total = sum(archaic.values())
    if total_words and arch_total / total_words * 1000 > 3:
        top = ", ".join(f"{k} {v}" for k, v in archaic.most_common(5) if v)
        warnings.append(f"book: {arch_total} archaic words in {total_words} (budget ~1 per 1,000). Most used: {top}")

    if not quiet:
        for w in warnings:
            print("WARNING ", w)
    for e_ in errors:
        print("ERROR   ", e_)
    print()
    print(f"{len(E)} entries, {total_words} words, {len(errors)} errors, {len(warnings)} warnings")
    if skill_use:
        print("check options by skill (published book: each skill 55–70, evenly spread):")
        for k, v in sorted(skill_use.items(), key=lambda kv: -kv[1]):
            print(f"  {k:20} {v}")
    if awarded or checked:
        print("story tokens:")
        for tok in sorted(set(awarded) | set(checked)):
            print(f"  #{tok:<3} awarded at {sorted(awarded.get(tok, []))}  mentioned at {sorted(checked.get(tok, []))}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
