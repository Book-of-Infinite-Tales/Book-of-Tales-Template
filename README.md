# Book of Tales Template

A starting point for creating your own collection of custom Books of Tales for *Tales of the Arthurian Knights*, loadable in the [Book of Infinite Tales](https://book-of-infinite-tales.github.io) reader.

Fork this repository, replace the example content with your own passages, and share the result with other players. If you like, submit your collection to the [Library of Infinite Tales](https://github.com/RobMcA/Library-of-Infinite-Tales) registry so it appears in the reader's community section.

---

## What's in this repository

```
books.json                                       ← lists all your books
tales-of-the-arthurian-knights-components.json  ← game components (ages, characters, etc.)
example-book/
  book.json                                      ← your first book's passages
```

**`books.json`** is the index the reader loads first. It lists each of your books by subdirectory path. Add a new entry here every time you create a new book.

**`tales-of-the-arthurian-knights-components.json`** describes the physical game components — Ages, Terrains, Feature cards, Character cards, Milieu cards, Locations, Quests. This file is shared by all your books. You won't need to edit it often.

**`[book-name]/book.json`** is the actual book. It contains all the passages (entries) a player reads during an encounter, plus a reference to the components file.

---

## Getting started with Claude

The fastest way to set up and write books is to paste the prompts below into Claude (claude.ai or Claude Code). There are two prompts:

1. **Setup prompt** — run once after forking to configure your collection.
2. **Book creation prompt** — run once per book to generate a complete set of passages, add it to your collection, and publish it.

---

## Prompt 1 — One-time collection setup

After forking this repository, paste the following into Claude. Fill in the bracketed fields before sending.

```
I've just forked https://github.com/RobMcA/Book-of-Tales-Template to my own
GitHub account. Please help me set up my collection.

My GitHub username: [YOUR_GITHUB_USERNAME]
My fork's repo name: [YOUR_REPO_NAME]
My collection title: [e.g. "The Knights of the Vale — Books of Tales"]
My name (for author fields): [YOUR_NAME]

Please:
1. Show me the git clone command to check out my fork locally.
2. Update books.json: replace "My Book of Tales Collection" with my collection
   title, and "Your Name" with my name.
3. Rename the example-book directory to the name of my first book
   (using lowercase-with-hyphens, e.g. "the-forest-witch") and update the
   path in books.json to match.
4. Update example-book/book.json (now renamed): set the title, author, and
   description fields.
5. Show me the git commands to commit and push these changes.
6. Tell me how to verify everything works: open
   https://book-of-infinite-tales.github.io and enter
   [YOUR_GITHUB_USERNAME]/[YOUR_REPO_NAME] to confirm my collection loads.
```

---

## Prompt 2 — Create a new book

Paste the following into Claude each time you want to add a new Book of Tales to your collection. Fill in every bracketed field — the more detail you give about the encounter theme, the better the generated passages will be.

```
I'm adding a new Book of Tales to my collection at
https://github.com/[USERNAME]/[REPO-NAME].
My local clone is checked out at [LOCAL PATH TO REPO].

== About this encounter ==

Theme / central figure: [e.g. "a mysterious ferryman who demands a secret
before he will carry the knight across the river"]

Book directory name: [lowercase-with-hyphens, e.g. "the-ferryman"]
Display title: [e.g. "The Ferryman"]
Author: [YOUR NAME]
Description (one sentence): [e.g. "A ferryman on a dark river tests the
knight's honesty before granting passage."]

Encounter card types to support:
  Character encounters? [YES/NO] — if yes, list which character(s) by name
  Milieu encounters?    [YES/NO] — if yes, list which milieu(s) by name
  Location encounter?   [YES/NO] — if yes, give the location name
  Quest?                [YES/NO] — if yes, describe the quest

Ages to cover: [ALL THREE / AGE 1 AND 2 ONLY / etc.]

Tone: [e.g. "eerie and melancholy, with moments of dark humour"]

== Format reference ==

A book lives at [BOOK-DIRECTORY]/book.json. Structure:

{
  "schema": "book-of-infinite-tales/v1",
  "title": "...",
  "author": "...",
  "version": "0.1.0",
  "description": "...",
  "components": "../tales-of-the-arthurian-knights-components.json",
  "entries": [ ... ]
}

Entries are passages. The standard encounter flow is:

  Response passage  →  Resolution passage  →  (outcome with rewards)

RESPONSE PASSAGE: Second-person narrative setting the scene, ending with
2–4 italic choices in "responses[]". Each choice points ("goto") to its
own resolution passage. Nearly every response should go to a resolution
(skill check), not directly to a result.

RESOLUTION PASSAGE: Short narrative. One or more "resolutions[]" — each
is one way to attempt the encounter. Each resolution has:
  "using": array of skill names, skill categories, or renown types
  "target": a number (fixed), or {"base":N,"addLocationNumber":true} (variable)
  "success": { "body": "...", "rewards": { ... } }
  "failure": { "body": "...", "rewards": { ... } }

Both success AND failure must award at least "destiny": 1.

Skills (use exact capitalisation):
  Martial:    Warfare, Sword & Shield, Mounted, Hunting
  Spiritual:  Piety, Wisdom, Honor, Magic
  Courtly:    Diplomacy, Cunning
  Wilderness: Nature Lore, Endure Hardship
  Categories: Martial, Spiritual, Courtly, Wilderness (allows any skill in group)
  Renown:     Divinity, Romance, Villainy, Any

Rewards: destiny (number or "location_number"), renown ([{type, delta}]),
skills ([{name} or {category, count}]), treasures (number or named string),
statuses ([{action:"gain"|"lose", name}]), storyToken (string),
movement (number or "free").

Passage numbering conventions:
  Age starts:  1000, 2000, 3000
  Epilogue:    9999
  Character:   character.base + feature.offset  (e.g. base 1400 + offset 5 = 1405)
  Milieu:      age.milieuBase + milieu.terrainOffset
  Location:    the 4-digit id printed on the card

== Components available ==

Paste the contents of tales-of-the-arthurian-knights-components.json here,
OR describe which specific character(s), milieu(s), or location you are
writing for and their base/offset numbers.

[PASTE COMPONENTS JSON OR DESCRIBE WHAT YOU ARE WRITING FOR]

== What I need ==

1. Create [BOOK-DIRECTORY]/book.json with a complete set of entries:
   - Age-start passages (1000, 2000, 3000) if covering all three ages
   - Full encounters: for each character/feature combination, a response
     passage and one resolution passage per response choice
   - Milieu passages for each supported terrain × age combination
   - Location passage (and per-age Place of Power passages) if applicable
   - Quest passage if applicable
   - Epilogue (9999) if not already present in another book

2. Add my new book to books.json:
   {"path": "[BOOK-DIRECTORY]", "title": "...", "description": "..."}

3. Show me the git commands to commit and push.

4. Tell me how to test: open https://book-of-infinite-tales.github.io,
   enter [USERNAME]/[REPO-NAME], navigate to my new book, and step through
   a full encounter to confirm it works.

5. Tell me how to optionally submit to the Library of Infinite Tales:
   open a PR at https://github.com/RobMcA/Library-of-Infinite-Tales adding
   my entry to registry.json.
```

---

## Manual reference

If you prefer to write your own passages without Claude, see [`docs/book_format.md`](docs/book_format.md) in this repository. It covers every field in detail with examples.

The short version:

| File | Purpose |
|---|---|
| `books.json` | Index of all books in your collection. Add one entry per book directory. |
| `tales-of-the-arthurian-knights-components.json` | Game components. Edit this to add Locations and Quests as you write passages for them. |
| `[book]/book.json` | The passages. Every entry needs an `id` and `body`. Add `responses`, `resolutions`, and `rewards` as needed. |

---

## Testing your collection

Open [book-of-infinite-tales.github.io](https://book-of-infinite-tales.github.io) and enter:

```
your-github-username/your-repo-name
```

The reader will fetch your `books.json`, list your books, and let you open and navigate each one. If there is a validation error the reader will show the error message with the field that failed.

---

## Submitting to the Library of Infinite Tales

Once your collection is published and loads without errors, you can submit it to the [Library of Infinite Tales](https://github.com/RobMcA/Library-of-Infinite-Tales) so it appears in the reader's community section.

Open a pull request adding your entry to `registry.json`:

```json
{
  "repo": "your-github-username/your-repo-name",
  "title": "Your Collection Title",
  "author": "Your Name",
  "description": "One sentence describing your collection.",
  "tags": ["optional", "tags"]
}
```

See the [contributing guide](https://github.com/RobMcA/Library-of-Infinite-Tales/blob/main/CONTRIBUTING.md) for full instructions.

---

## License

The template structure and example passages in this repository are released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) — public domain. Use them freely as the basis for your own books.

The *Tales of the Arthurian Knights* game system and its components are © WizKids and are not included here. Book authors are responsible for ensuring their content does not reproduce any copyrighted material.
