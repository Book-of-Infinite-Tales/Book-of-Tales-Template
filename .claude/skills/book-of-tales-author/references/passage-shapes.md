# Passage shapes

The shapes a passage can take, how often the published book uses each, and how to express each one in `book.json`. For prose, see style-guide.md. For numbers, see rewards.md.

## How the book is built

The published book has about 1,300 passages. Roughly:

| Kind | Share | What it is |
|---|---|---|
| Response | ~27% | Scene plus choices. Every formula passage (character × feature, milieu × terrain × age, Place of Power visits) is one of these. |
| Resolution | ~43% | Lead-in plus one or two skill checks, each with success and failure text. |
| Result | ~23% | Prose plus a fixed reward, no roll. "Tell me your story", walk-aways, blessings. |
| Special | ~7% | Gates, age starts, global events, epilogue, location card draws. |

**Passage IDs run consecutively; links scatter.** Within a thousand-block the book fills numbers in order (1001, 1002, 1003…). A character's block reserves 100 numbers and uses about 65. What is scattered is the *linking*. A response at 1001 leads to 2134, 1874 and 2555. Resolutions are not kept inside their character's hundred-block, or even its thousand-block. When you assign IDs:

- the formula IDs are fixed and reserved (run `scripts/generate-passage-list.py`);
- put resolution and result passages in the free IDs, **far** from their response;
- keep a ledger so no ID is used twice.

## 1. Response passage

**Use:** every encounter's entry point.

**Shape:** 1–3 paragraphs (median 150 words) → choices.

**Choices:** 2 in 68% of responses, 3 in 16%, 4 very rarely. A **single** choice (15%) is a "continue" after something has already happened: a gate was passed, or the knight was swept up in events.

A third choice is usually one of:
- **walk away** → a result passage (`Move 1 space`);
- **romance** → a resolution, marked romantic;
- **ask for the story** → a result passage with lore and a small reward;
- **a third moral road**, for example at a trial: mercy, strict law, or blame the accuser.

```json
{
  "id": "1015",
  "body": "As you ford a shallow river at dusk, …\n\n\"Good knight!\" he calls. …",
  "responses": [
    { "label": "You may help King Ederyn win back his crown.", "goto": "1377" },
    { "label": "You may instead visit the goose-girl and bargain for the crown on your own account.", "goto": "2048" }
  ]
}
```

**Conditional choices.** Some choices are only open to certain knights, for example *"If this is the Age of the Quest of the Holy Grail, you may…"* or *"If you are not Unhorsed, you may…"*. The reader cannot hide an option, so put the condition at the front of the label, and the player applies it:

```json
{ "label": "If this is the Age of the Quest of the Holy Grail, you may ask the anchoress for counsel in your search.", "goto": "1332" }
```

## 2. Resolution passage

**Use:** the destination of most choices.

**Shape:** lead-in (0–3 sentences, median 35 words) → 1 or 2 check options (2 in 69% of resolutions) → success and failure per option.

Each option tests one of the following:

| Option kind | Print form | `using` | How common |
|---|---|---|---|
| One skill | *Cunning (4)* | `["Cunning"]` | most options |
| Either of two skills | *Piety or Magic (5)* | `["Piety", "Magic"]` | ~60 in the book |
| Any skill in a category | *1 Martial Skill of your choice (4)* | `["Martial"]` | ~45 |
| Renown ranks | *your ranks in Romance*: 4 or higher succeeds | `["Romance"]`, target = the threshold | ~40 |
| Category total | *Total Wilderness Skill*: the sum of all three skills | `["Wilderness"]` plus label text, see below | ~15 |

```json
{
  "id": "1377",
  "body": "\"No goose-girl in Britain can outwit a king and a knight together,\" you say, hauling Ederyn to his feet. …",
  "resolutions": [
    {
      "label": "win the crown back at dice",
      "using": ["Cunning"],
      "target": 4,
      "success": { "body": "…", "rewards": { "destiny": 2, "skills": [{ "category": "Courtly" }], "renown": [{ "type": "Villainy", "delta": 1 }] } },
      "failure": { "body": "…", "rewards": { "skills": [{ "name": "Cunning" }], "statuses": [{ "action": "gain", "name": "Scorned" }] } }
    },
    {
      "label": "persuade Wenna to return it",
      "using": ["Diplomacy"],
      "target": { "base": 3, "addLocationNumber": true },
      "success": { "body": "…", "rewards": { "destiny": "location_number", "skills": [{ "category": "Courtly" }], "renown": [{ "type": "Any", "delta": 1 }] } },
      "failure": { "body": "…", "rewards": { "skills": [{ "name": "Diplomacy" }] } }
    }
  ]
}
```

**Labels** are lowercase verb phrases naming the deed: "win the crown back at dice", not "Cunning". The reader shows the skill beside the label.

**Two options should differ in kind:** force vs wit, faith vs cunning, fighting on horseback vs on foot. Don't offer two skills from the same category for the same deed.

### Renown checks with bands

The published book often grades a renown check in three bands: *4 or more ranks* (best), *2–3 ranks* (middling), *0–1 ranks* (failure). The schema has one threshold, so:
- `target` = the top band's threshold (3–5; 4 is most common);
- `success` = the top band;
- `failure` = the middle band's text, with any extra penalty for the bottom band as a bracketed line: `[If you have 0–1 Ranks of Romance, you also become Scorned.]`

Renown checks are not rolled, so mention in the label that the knight is drawing on reputation: "recount your deeds of love".

### Category-total checks

The book sometimes asks for the knight's *total* in a category (all three skills added together), against a higher target that often grows with the Age # ("5 + Current Age #"). The schema tests one skill from the category, so:
- `using: ["Martial"]`;
- say so in the label: "hold the line (use your Total Martial Skill: all three Martial skills added together)";
- set the target 3–4 higher than a single-skill check would be. For "+ Current Age #", pick the number for the age the passage belongs to, or put the rule in the label.

Use this for grand trials of a whole way of life: a battle, a courtship of a queen, a season in the wild. Keep it rare.

## 3. Result passage

**Use:** asking for a story, accepting a gift, a blessing, a farewell, walking away.

**Shape:** prose (median 80 words) → `rewards`. No choices, no checks.

```json
{
  "id": "1874",
  "body": "\"Nine winters I have kept this bridge,\" the old toll-keeper says, …",
  "rewards": { "destiny": 1, "skills": [{ "name": "Nature Lore" }] }
}
```

Walk-away results are one to three sentences with `"rewards": { "movement": 1 }`.

## 4. Gate passage (conditional at the top)

**Use:** stopping a repeat encounter, following up a thread, or redirecting in a particular age. It sits at the top of a response or resolution:

> *If you have Story Token #14, turn immediately to 1976. Otherwise, gain Story Token #14 and continue reading below.*

The reader has no conditional logic, so split it into two entries:

```json
{
  "id": "2013",
  "body": "At the edge of a salt marsh, you find a pavilion hung with black and silver …",
  "responses": [
    { "label": "If you have Story Token #14, turn to the tale that follows your last visit.", "goto": "1976" },
    { "label": "Otherwise, continue.", "goto": "2084" }
  ]
}
```

Then `2084` carries on the scene, with `"rewards": { "storyToken": 14 }` on the entry, then its own choices. Put the setting sentence in the gate passage so the player knows where they are before choosing.

Other gates the book uses:
- **Age:** *If this is the Age of the Final Wars of Britain, turn immediately to 1651.* Used about 8 times.
- **Redraw:** *If any player is on the quest "Escort the Queen", discard this Feature card, draw a new one and turn to that encounter.* Rare. It stops an encounter contradicting a quest in progress. In JSON, write it as a sentence in the body. It needs no response option.
- **Status:** *If you are Betrothed…*, *If you are Unhorsed…*. Mostly used as a reward modifier inside a bracket, not as a gate.

## 5. Outcome that continues

**Use:** when success or failure opens a second decision instead of ending the scene. About 10 outcomes in the book end by offering two new choices (*You may either "go after him" or "let him go"*), and several use named sub-sections (*Read "Press on" below*).

Keep it rare. In JSON, the outcome gets a `goto` to a small response passage that holds the two choices, or directly to the named follow-on passage:

```json
"failure": {
  "body": "… He shoulders past you toward the stair, and you hear his sword clear its scabbard.",
  "rewards": { "skills": [{ "name": "Cunning" }] },
  "goto": "1590"
}
```

where `1590` is a response passage with two choices and a one-sentence body.

## 6. Unusual shapes

Each appears a handful of times. Use them as spice, not as structure.

- **Reward first, then the check.** *Gain Story Token #N. You may use Warfare to…* The entry has both `rewards` and `resolutions`.
- **Choice inside an outcome.** *You may "cut the prisoner loose" or "leave him bound".* Map it as shape 5.
- **Named sub-sections.** A passage offers "Press on" or "Give up the chase" after the rolls. Each sub-section becomes its own entry, reached by `goto`.
- **A choice between two treasures, statuses or gifts.** *Draw 2 Treasure cards, keep one.* *Select one of these Status cards.* Write it in the body as a bracketed instruction.
- **Map objectives.** *Place one of your Quest Markers and the story token on a named city. After an encounter there, remove them and claim the reward.* See story-tokens-and-renown.md. Write it in the body as a bracketed instruction.
- **Global events.** *Every Knight at Camelot gains…* Used about 24 times, mostly in age starts and grand set pieces. Write in the body.

## 7. Special passages

- **Age start (1000, 2000, 3000).** A global scene every player hears. It sets up the age's crisis, offers each knight three ways to respond (one per renown), and gives scoring or setup instructions. Result shape: no choices, no checks. See world-and-characters.md for the three ages.
- **Epilogue (9999).** End-of-game scoring by renown, and a closing paragraph chosen by which renown the table accumulated most. Result shape.
- **Location card draw (26xx).** Short, usually a dream or summons, plus permission to enter the location. About 60–100 words.
- **Place of Power visit (25xx, one per age).** A full response passage, often with three choices. These are the grandest scenes in the book: Avalon, the Grail Castle, the Green Chapel.
- **Quest and status encounters.** Body exactly `Refer to physical Book of Tales for this passage.` with no rewards.

## Mechanics the schema can't express

Write these as a final bracketed line in the body, in the book's reward grammar, and keep everything else in `rewards`:

| Mechanic | Bracket text |
|---|---|
| "Skill of your choice" from any category | `[Gain 1 Skill of your choice]` (or use a category in `skills`) |
| Destiny = N + Location # | `"destiny": "location_number"` plus `[Gain N additional Destiny]` |
| Destiny = Age #, Obsessed number, highest rank | `[Gain Destiny equal to …]` |
| Skill Marker on the Accompanied card | `[Place a Hunting Skill Marker on your Accompanied Status Card]` |
| Move to a named place or by sea | `[You may immediately move up to 3 spaces by Sea]` |
| Draw a Quest Card | `[Draw 1 Quest Card]` |
| Lose all ranks of a renown | `[Lose all Ranks of Villainy]` |
| Remove any unwanted status | `[You may remove 1 unwanted Status Card]` |
| Conditional add-on | `[If you are Betrothed, gain 1 Rank of Villainy]` |
