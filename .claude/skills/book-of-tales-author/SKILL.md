---
name: book-of-tales-author
description: Write an original Book of Tales for the board game Tales of the Arthurian Knights, in the voice and structure of the published book, as a book.json the Book of Infinite Tales reader can load. Use when generating a new book, drafting or revising passages, designing encounters, choosing skill checks and rewards, planning story tokens, or reviewing a book for style. Covers themes and cast, plot patterns, passage shapes, reward calibration, story tokens, renown, and a detailed prose style guide.
---

# Book of Tales Author

This skill helps you write a **new, original** Book of Tales that plays and reads like the one printed with *Tales of the Arthurian Knights*. It rests on an analysis of the published book: 1,284 passages, about 470,000 words, transcribed from photographs and measured passage by passage. The numbers in these files are counts from that analysis, not guesses.

**This skill contains no text from the published book, and nothing you write with it should either.** The published book is copyrighted. Use it for patterns: how long passages run, what the choices look like, how rewards are sized, how a scene is paced. Do not reproduce its passages, its plots told beat for beat, or its original characters. Every example passage in this skill was written fresh to show the style.

## Reference files

Read them in this order the first time. After that, open the one you need.

| File | Read it when |
|---|---|
| [references/style-guide.md](references/style-guide.md) | **Always, before writing any prose.** Voice, rhythm, dialogue, how outcome pairs are built, and what goes wrong. |
| [references/passage-shapes.md](references/passage-shapes.md) | Designing an encounter's structure, or turning prose into `book.json`. |
| [references/rewards.md](references/rewards.md) | Setting targets, choosing skills, sizing rewards, assigning statuses. |
| [references/story-tokens-and-renown.md](references/story-tokens-and-renown.md) | Planning threads across encounters, or anything that checks or changes renown. |
| [references/world-and-characters.md](references/world-and-characters.md) | Building the cast, setting an age's mood, or choosing who a character card becomes. |
| [references/plots.md](references/plots.md) | Choosing a plot for an encounter slot. |

`scripts/lint_tales.py` checks a finished `book.json` against the house rules in this skill (see step 6 below).

## The ten rules that matter most

1. **Second person, present tense, and it moves.** "You come upon…", "The king laughs and…". Something happens in every paragraph.
2. **People talk.** About a fifth of the book is dialogue. Named characters speak in their own voices. A passage with nobody speaking is usually a milieu passage or a short result.
3. **Every response ends in choices that start with "You may"** and name a *deed*, never a skill: "You may help the ferryman", not "You may use Diplomacy".
4. **Choices are real forks, and usually moral ones:** help or rob, serve or oppose, mercy or law. Two choices is the norm (68%); three when there is a genuine third road, often walking away or a romantic option.
5. **The resolution is where the skills appear.** One or two skills, each with its own target and its own success and failure text.
6. **Success and failure for a skill start from the same moment.** Often they open with the same sentence, then split apart.
7. **Failure teaches.** A failed check almost always gains a skill: usually the one tested, sometimes the lesson the scene actually taught. It rarely grants Destiny. See rewards.md.
8. **Rewards are sized by the table in rewards.md**, not by feel: 2–4 items on a success, 1–2 on a failure.
9. **Never write the player characters.** The eight playable knights and dames are Sir Lancelot, Sir Palomides, Sir Gawain, Sir Percival, Sir Galahad, Sir Tristan, Dame Enid and Dame Bradamante. The published book never names any of them, because "you" might be any of them. Arthur, Guinevere, Merlin, Kay, Mordred, Morgan and a large supporting cast are fair game.
10. **Plain modern prose with a light old-fashioned seasoning.** "Good knight" is the standard form of address. Words like *prithee*, *'tis* and *thee* are rare spices, used in dialogue by old or grand speakers. See the style guide for the exact budget.

## Workflow

### 1. Read the components and list the required passages

From the repo root:

```bash
python scripts/generate-passage-list.py tales-of-the-arthurian-knights-components.json
```

This lists every passage the book must contain: age starts (1000, 2000, 3000), 132 character encounters (12 characters × 11 features, at `character.base + feature.offset`), 162 milieu encounters (3 ages × 9 milieus × 6 terrains), locations and Places of Power, quests, status encounters, and the epilogue (9999). All names you use must match the components file exactly.

Quest and status-encounter passages depend on physical cards. Their body must be exactly `Refer to physical Book of Tales for this passage.` with no rewards.

### 2. Write a short book bible before any passages

Settle these first, because they shape every passage that follows:

- **Title and tone.** One sentence of tone per age (see world-and-characters.md for how the published book frames each age).
- **The recurring cast.** 10–20 named characters who will appear in more than one passage, with a line on each one's voice. Most encounters invent a fresh minor character as well. That is normal: the published book names about 200 people.
- **Story-token plan.** Decide which tokens (1–30) you will use and for what. See story-tokens-and-renown.md. Record each as *awarded at → checked at*.
- **Plot slate.** For each character card and each milieu, pick plot patterns from plots.md so that neighbouring encounters don't repeat a shape.
- **ID ledger.** The formula passages are reserved. Resolution and result passages go in the free numbers. Keep a running list of which numbers you've used.

### 3. Draft encounter by encounter

For each encounter, write the response passage and every passage its choices lead to, together in one pass. Then move on. Use the shapes in passage-shapes.md and the voice in style-guide.md.

Number resolution passages so they are **not** adjacent to their response. A player looking up 1305 should not see 1306 and learn the outcome. The published book scatters them widely, even across character blocks, so a response at 1305 may lead to 1142 and 2210.

### 4. Set the mechanics

For each resolution:
- choose one or two skills that fit the *deed* (rewards.md has the skill-selection table),
- set a target: fixed 3–6, or a base of 2–4 plus the Location #,
- write the rewards from the success and failure tables.

Keep the whole book's skill use balanced. The published book uses each of the 12 skills between 55 and 70 times.

### 5. Write the JSON

Follow the mappings in passage-shapes.md. Put mechanics the schema can't express (a map move to a named city, a Quest Marker, a Skill Marker on the Accompanied card) as a final bracketed instruction line in the body. Keep everything the schema *can* express in `rewards`.

Set `"aiGenerated": true` in the manifest.

### 6. Check it

```bash
python .claude/skills/book-of-tales-author/scripts/lint_tales.py path/to/book.json
python scripts/add_entries.py path/to/book.json new-entries.json   # when merging batches
```

The lint script catches mechanical slips: a failure that teaches nothing, a response label without "You may", a banned name, a target out of range, prose that is too long or short, and heavy archaism. Then open the book in the reader (https://book-of-infinite-tales.github.io) and play a few encounters end to end.

### 7. Read it aloud

The final test is the one in the style guide: read a response and one of its resolutions aloud. If it sounds like a story told at a table, with people, a problem, a choice and a consequence, it's right. If it sounds like an essay about a story, rewrite it.

## Other guidance in this repo

`CREATE_BOOK.md` follows this skill. Two other files carry older authoring conventions in places:

| Topic | Older guidance | This skill (measured from the published book) |
|---|---|---|
| Skills per check | `docs/book_format.md`: exactly one `using` entry | one skill, one category, one renown type, or a pair of skills. "A or B" pairs appear about 60 times. |
| Failure rewards | `README.md` Prompt 2: at least 1 Destiny on every outcome | the skill alone is typical, often with a negative status. Destiny on failure is rare (12%). |
| Response length | `docs/book_format.md`: 2–5 paragraphs | median about 150 words: usually 1–3 paragraphs |
| Walk-away option | `docs/book_format.md`: must carry a negative reward | usually a neutral `Move 1 space`, sometimes a small cost |
| Where linked passages go | `docs/book_format.md`: the same thousand-block | anywhere, as long as they are not adjacent |

The reader accepts either convention, so both validate. For the JSON schema itself, `docs/book_format.md` is authoritative. For how to write, follow this skill.
