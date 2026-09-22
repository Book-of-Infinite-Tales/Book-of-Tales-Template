# Create Book

You are writing a new, original Book of Tales for *Tales of the Arthurian Knights*: a set of numbered passages the Book of Infinite Tales reader can load. The book should read and play like the published Book of Tales, but every word of it must be your own.

**Use the `book-of-tales-author` skill for all of this work.** It lives in `.claude/skills/book-of-tales-author/` and holds the style guide, passage shapes, reward calibration, story-token and renown rules, the world and cast, plot patterns, and a lint script. Where this file and the skill differ, the skill wins. Read `docs/book_format.md` for the JSON schema.

Use `./tales-of-the-arthurian-knights-components.json` as the components file.

## Model and effort

A full book runs to 1,000+ passages and several hundred thousand words, so it takes many sessions, not one. The book bible and ID ledger are what keep it consistent across them. Pick the model and effort for each phase:

| Phase | Model | Effort | Why |
|---|---|---|---|
| Title, style, ages and book bible (Process 1–4) | Opus | High | Every later passage depends on these decisions, and they are little text, so the cost is small. |
| Drafting passages (Generating 2) | Opus for quality, or Sonnet to save money | Medium | Voice and moral forks are where a stronger model shows. More effort mostly adds cost, since this is writing more than reasoning. |
| Mechanics and JSON (targets, rewards, IDs) | Sonnet | Medium | Table lookups from `references/rewards.md` and careful bookkeeping. |
| Lint fixes and balance passes (Generating 3) | Sonnet or Haiku | Low–Medium | The lint script finds the problems. The model only fixes them. |

- Work one age or one character card per session, and re-read the book bible and `references/style-guide.md` at the start of each.
- To save money, draft with Sonnet, then have Opus review each age for style.
- Don't use Haiku for prose. It drifts from the style guide's finer rules, such as success and failure opening from the same moment, and the archaism budget.

## Process

1. **Title.** Ask for the title of the book.
2. **Style.** Based on the title, suggest a tone for the book, built on the skill's style guide, and ask whether the user would like it or wants to describe their own. The house style (concrete, dialogue-led, second person, often funny, sometimes dark) is the default. A user's tone changes the flavour, not the structure.
3. **Ages.** Write a short guiding narrative for each of the three ages: the Golden Age of Camelot, the Quest of the Holy Grail and the Final Wars of Britain (see `references/world-and-characters.md`). Ask whether to use them, change them, or replace them with the user's own.
4. **Book bible.** Before writing passages, draft and show the user:
   - the recurring cast (10–20 named characters with a line on each one's voice);
   - 10 story ideas per age: overarching tales that will surface in the bigger encounters;
   - the story-token plan (which tokens, what earns each, where each is checked);
   - a plot slate: a pattern from `references/plots.md` for each character-and-feature encounter.
5. **Generate** the book (see below) and save it as `book.json` in a new subdirectory named after the title (lowercase, hyphenated). Add it to `books.json`.

## Generating

Tell the user as you start each step.

### 1. Passage list

```
python scripts/generate-passage-list.py tales-of-the-arthurian-knights-components.json
```

### 2. Passages, in this order

1. **Age starts** (1000, 2000, 3000) and the **epilogue** (9999).
2. **Character encounters.** For each one, write the response passage and every passage its choices lead to before moving on.
3. **Milieu encounters,** grouped by age. For about half, reuse an opening frame across the three ages and change what the knight finds (see the skill).
4. **Locations** (card draw) and their **Places of Power** (one visit per age). These are the grandest scenes.
5. **Quest and status encounters.** Don't write these (see the rules below).

For each encounter, draw on the age's story ideas when one fits naturally. Otherwise, take the character card, feature and plot slate as the seed.

Work in batches (for example, one character card at a time), merge each batch with `scripts/add_entries.py`, and run the lint script after each one.

### 3. Check and save

```
python .claude/skills/book-of-tales-author/scripts/lint_tales.py <book-dir>/book.json
```

Fix every error and read the warnings. Set `"aiGenerated": true` in the manifest.

---

## Rules: follow these exactly

These summarise the skill. The full reasoning and the measurements behind them are in the skill's reference files.

### Originality
- Write everything fresh. Never reproduce, closely paraphrase, or retell beat by beat any passage from the published Book of Tales, and don't reuse its invented characters. Figures of legend (Arthur, Merlin, Morgan, Kay, Mordred and so on) are free to use in your own words.
- **Never name the player characters:** Sir Lancelot, Sir Palomides, Sir Gawain, Sir Percival, Sir Galahad, Sir Tristan, Dame Enid and Dame Bradamante. The reader may be any of them.

### Quest and status passages
Quest passages and status-encounter passages depend on the physical cards. Their body must be exactly `Refer to physical Book of Tales for this passage.` with no rewards.

### Voice
- Second person, present tense. Something happens in the first two sentences.
- Named characters who speak. About a fifth of the text is dialogue.
- Plain modern narration, with archaism only as a light seasoning in dialogue (about one archaic word per thousand words).
- No essay sentences about what a scene means, and no aphorisms.

### Response passages
- Body: typically **80–300 words** (1–3 paragraphs).
- **2 choices** is the norm. A 3rd is fine when it is a genuine road: walking away, a romantic option, asking for someone's story, or a third verdict. 4 is very rare.
- Every choice starts **"You may"** and names a deed, **never a skill**. Romantic choices start `* ` and set `"romantic": true`.
- A walk-away leads to a short result passage, usually `"movement": 1`, sometimes with a small cost.
- "Ask about their story" leads to a result passage: lore, told in character, with a small reward.

### Resolution passages
- Lead-in: **0–3 sentences**. The knight commits to the choice, often in speech.
- **1 or 2 check options**, different in kind (force against wit, faith against cunning).
- `using` holds **one skill, one category, one renown type, or a pair of skills** that suit the same deed equally (for example `["Piety", "Magic"]`).
- Targets: fixed **3–6** (4–5 standard, 7–8 legendary), or `{ "base": 2–4, "addLocationNumber": true }`, with base 3 the most common.
- Each outcome body: typically **40–220 words**. Success and failure for an option start from the same moment and split cleanly.

### Rewards
- **Success:** usually 2–4 items. Destiny (2–4, or `"location_number"` for location-scaled checks), a skill of choice from the tested category, and 1–2 ranks of renown, with a status or treasure for bigger deeds.
- **Failure:** the knight learns. It gains the tested skill (or the category, or the lesson the scene taught), often with a negative status. Failures **usually grant no Destiny**, and a failure's Destiny must always be less than the success's.
- The renown track follows the **deed**, not the skill. Villainous roads should be genuinely rewarding (more Destiny, more treasure), with the cost falling elsewhere.
- Use only names from the components file for statuses, treasures and story tokens. For your own threads, use story tokens without printed notes: 1, 2, 3, 7, 12–20, 27–30.
- Write conditional jumps as passage links: `If you have Story Token #14, turn immediately to [[1976]].` The player follows the link when the condition applies.
- Use the structured fields where they fit: formula Destiny and targets (`{ "base": 1, "addLocationNumber": true }`, `addAgeNumber`), `"partial"` for graded renown checks, `"total": true` for category totals, and a list of tracks for "Divinity or Romance". Anything else goes in the reward's `notes`, for example `"Place a Hunting Skill Marker on your Accompanied Status Card"`.

### Passage ID management
The formula IDs (character + feature, milieu, location, Place of Power, quest, status, age starts, epilogue) are reserved. Resolution and result passages use **free IDs**. Keep a running list of the IDs you assign. **Never place a linked passage next to the one that leads to it.** Scatter them widely, even into other character blocks, so glancing at a neighbouring number never spoils an outcome.
