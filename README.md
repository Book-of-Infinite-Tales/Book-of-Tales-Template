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

## Manual reference

See [`docs/book_format.md`](docs/book_format.md) in this repository for every field in detail with examples.

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

## Sharing your collection

To share your collection with the community, see the [Library of Infinite Tales](https://github.com/RobMcA/Library-of-Infinite-Tales) — a registry of community books that appear in the reader's community section.

---

## License

The template structure and example passages in this repository are released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) — public domain. Use them freely as the basis for your own books.

The *Tales of the Arthurian Knights* game system and its components are © WizKids and are not included here. Book authors are responsible for ensuring their content does not reproduce any copyrighted material.
