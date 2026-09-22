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

**Conditional choices.** Some choices are only open to certain knights, for example *"If this is the Age of the Quest of the Holy Grail, you may…"* or *"If you are not Unhorsed, you may…"*. Put the condition at the front of the label. The player applies it:

```json
{ "label": "If this is the Age of the Quest of the Holy Grail, you may ask the anchoress for counsel in your search.", "goto": "1332" }
```

## Passage links

Write `[[1234]]` anywhere in an entry body, an outcome body or a reward note, and the reader shows it as a link to passage 1234. `[[1234|the war council]]` shows your own link text. This is how the book's conditional jumps work: the passage states the condition, and the player follows the link if it applies. The reader never needs to know what the knight holds.

- Use links for gates (section 4), for outcomes that continue (section 5), and for any "turn to" in the prose.
- Don't put links in response or resolution labels. A response already leads to its `goto`, and the validator rejects links there.
- Every link must point to an existing passage. The reader's validator and `lint_tales.py` both check.

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
| Category total | *Total Wilderness Skill*: the sum of all three skills | `["Wilderness"]` with `"total": true` | ~15 |

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

### Targets

A target is a plain number (fixed), or a formula that adds the knight's Location # and/or the current Age #:

| Print form | `target` |
|---|---|
| *Cunning (4)* | `4` |
| *Hunting (3) + Location #* | `{ "base": 3, "addLocationNumber": true }` |
| *Total Courtly Skill (5 + Current Age #)* | `{ "base": 5, "addAgeNumber": true }` |

### Renown checks with bands

The published book often grades a renown check in three bands: *4 or more ranks* (best), *2–3 ranks* (middling), *0–1 ranks* (failure). Use `partial` for the middle band:

```json
{
  "label": "recount your deeds of love",
  "using": ["Romance"],
  "target": 4,
  "success": { "body": "…", "rewards": { "destiny": 3, "renown": [{ "type": "Romance", "delta": 1 }] } },
  "partial": { "min": 2, "body": "…", "rewards": { "destiny": 1 } },
  "failure": { "body": "…", "rewards": { "statuses": [{ "action": "gain", "name": "Scorned" }] } }
}
```

- `target` is the top band's threshold (3–5; 4 is most common). `partial.min` is the middle band's floor and must be below it.
- The reader shows three outcomes and labels the middle one "Partial (2+ Ranks)".
- Renown checks are not rolled, so say in the label that the knight is drawing on reputation.
- `partial` also works for rolled checks with a middle result, but the book rarely uses it that way.

### Category-total checks

The book sometimes asks for the knight's *total* in a category (all three skills added together), against a higher target that often grows with the Age #. Set `"total": true`:

```json
{
  "label": "hold the line against the host",
  "using": ["Martial"],
  "total": true,
  "target": { "base": 5, "addAgeNumber": true },
  "success": { "body": "…", "rewards": { "destiny": { "base": 3, "addLocationNumber": true }, "renown": [{ "type": "Any", "delta": 1 }] } },
  "failure": { "body": "…", "rewards": { "skills": [{ "category": "Martial" }] } }
}
```

The reader shows "Total Martial Skill" with a reminder to add the three skills together. `using` must hold skill categories. Set the target 3–4 higher than a single-skill check would be. Use this for grand trials of a whole way of life: a battle, a courtship of a queen, a season in the wild. Keep it rare.

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

**Use:** stopping a repeat encounter, following up a thread, or redirecting in a particular age. It sits at the top of a response or resolution, and is written with a link:

```json
{
  "id": "2013",
  "body": "At the edge of a salt marsh, you find a pavilion hung with black and silver.\n\nIf you have Story Token #14, turn immediately to [[1976]]. Otherwise, gain Story Token #14 and continue reading below.\n\nA herald in silver livery bars your way …",
  "rewards": { "storyToken": 14 },
  "responses": [
    { "label": "You may demand to see his lady.", "goto": "1422" },
    { "label": "You may offer the herald a wager.", "goto": "2280" }
  ]
}
```

- Put a setting sentence before the gate so the player knows where they are.
- A knight who follows the link never reads the rest, so the entry's `rewards` only apply to those who read on. Here that means only they gain the token.
- The published book's wording is the model: *If you have Story Token #N, turn immediately to [[…]]. Otherwise, gain Story Token #N and continue reading below.*

Other gates the book uses, all written the same way:
- **Age:** *If this is the Age of the Final Wars of Britain, turn immediately to [[1651]].* Used about 8 times.
- **Another player's token:** *If another player has Story Token #12, turn immediately to [[1340]].*
- **Renown or status:** *If you have 3 or more Ranks of Villainy, turn immediately to [[…]].*
- **Redraw:** *If any player is on the quest "Escort the Queen", discard this Feature card, draw a new one and turn to that encounter.* Rare. It stops an encounter contradicting a quest in progress. It needs no link.

## 5. Outcome that continues

**Use:** when success or failure opens a second decision instead of ending the scene. About 10 outcomes in the book end by offering two new choices, and several use named sub-sections (*Read "Press on" below*).

Keep it rare. Write the choices into the outcome with links:

```json
"failure": {
  "body": "… He shoulders past you toward the stair, and you hear his sword clear its scabbard. You may either go after him ([[1514]]) or return to your chamber ([[1743]]).",
  "rewards": { "skills": [{ "name": "Cunning" }] }
}
```

When there is only one way on, use `"goto"` on the outcome instead. The reader shows it as a Continue button.

## 6. Unusual shapes

Each appears a handful of times. Use them as spice, not as structure.

- **Reward first, then the check.** *Gain Story Token #N. You may use Warfare to…* The entry has both `rewards` and `resolutions`.
- **Choice inside an outcome.** *You may "cut the prisoner loose" or "leave him bound".* Use links, as in shape 5.
- **Named sub-sections.** A passage offers "Press on" or "Give up the chase" after the rolls. Each sub-section becomes its own entry, linked from the outcome.
- **A choice between two treasures, statuses or gifts.** *Draw 2 Treasure cards, keep one.* *Select one of these Status cards.* Use a reward note.
- **Map objectives.** *Place one of your Quest Markers and the story token on a named city. After an encounter there, remove them and claim the reward.* See story-tokens-and-renown.md. Use a reward note.
- **Global events.** *Every Knight at Camelot gains…* Used about 24 times, mostly in age starts and grand set pieces. Write in the body.

## 7. Special passages

- **Age start (1000, 2000, 3000).** A global scene every player hears. It sets up the age's crisis, offers each knight three ways to respond (one per renown), and gives scoring or setup instructions. Result shape: no choices, no checks. See world-and-characters.md for the three ages.
- **Epilogue (9999).** End-of-game scoring by renown, and a closing paragraph chosen by which renown the table accumulated most. Result shape.
- **Location card draw (26xx).** Short, usually a dream or summons, plus permission to enter the location. About 60–100 words.
- **Place of Power visit (25xx, one per age).** A full response passage, often with three choices. These are the grandest scenes in the book: Avalon, the Grail Castle, the Green Chapel.
- **Quest and status encounters.** Body exactly `Refer to physical Book of Tales for this passage.` with no rewards.

## Reward formulas and notes

Most of the book's reward grammar has a structured field. Use it:

| Print form | `rewards` |
|---|---|
| Gain Destiny = Location # | `"destiny": "location_number"` |
| Gain Destiny = 1 + Location # | `"destiny": { "base": 1, "addLocationNumber": true }` |
| Gain Destiny = Age # | `"destiny": { "base": 0, "addAgeNumber": true }` |
| 2 Ranks of Divinity or Romance | `"renown": [{ "type": ["Divinity", "Romance"], "delta": 2 }]` |
| 1 Rank of Renown | `"renown": [{ "type": "Any", "delta": 1 }]` |
| 1 Courtly Skill of your choice | `"skills": [{ "category": "Courtly" }]` |

Anything else goes in `notes`, one string per effect, written in the book's reward grammar. The reader prints each note inside the reward bracket, and notes may contain links:

```json
"rewards": {
  "destiny": 2,
  "notes": [
    "Place a Hunting Skill Marker on your Accompanied Status Card",
    "If you are Betrothed, gain 1 Rank of Villainy"
  ]
}
```

Typical notes: a Skill Marker on the Accompanied card; a move to a named place or by sea; *Draw 1 Quest Card*; *Lose all Ranks of Villainy*; *You may remove 1 unwanted Status Card*; *Gain Destiny equal to your highest Rank of Renown*; a conditional add-on such as *If you are Betrothed, gain 1 Rank of Villainy*; *On your next turn, turn to [[2134]]*.
