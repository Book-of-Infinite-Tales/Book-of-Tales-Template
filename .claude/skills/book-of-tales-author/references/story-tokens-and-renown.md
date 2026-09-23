# Story tokens and renown

Two systems carry a knight's history from one encounter to the next. Story tokens remember specific events. Renown remembers what kind of knight you are.

## Renown

### What the three tracks mean

| Track | Earned by | Typical deeds |
|---|---|---|
| **Divinity** | holiness, mercy, faith, sacrifice, service to the Grail | healing by prayer, sparing an enemy, returning stolen church goods, laying a ghost to rest |
| **Romance** | chivalry, courtly love, gallantry, the fame of fine deeds | courting, championing a lady, a splendid joust, reconciling lovers, a gracious gesture |
| **Villainy** | treachery, cruelty, greed, dark power, siding against Camelot | robbing the helpless, cheating, serving a rebel king, dark bargains with the fay |
| **Renown** (unspecified) | deeds that are simply *famous* | a hard-won victory, a clever solution. The player chooses the track. |

In `book.json`, unspecified renown is `{ "type": "Any", "delta": 1 }`.

**"X or Y" rewards are very common.** More than 200 rewards read *2 Ranks of Divinity or Romance* or *1 Rank of Romance or Villainy*. Write them as a list of tracks: `{ "type": ["Divinity", "Romance"], "delta": 2 }`. The player applies the whole delta to one track of their choice.

**Never grant two tracks at once.** The published book almost never does it (about 3% of renown rewards, several of them the conditional *If you are Betrothed* note). Don't write +1 Divinity *and* +1 Romance: write *1 Rank of Divinity or Romance*. Don't add a Rank of Renown on top of a named track either: the deed has already chosen the track. Losses alongside a gain are fine (*2 Ranks of Villainy | Lose 1 Rank of Divinity*). The book pairs the tracks as Divinity or Romance (most common), Romance or Villainy, and Divinity or Villainy, always in that order.

### How the book uses renown

**The deed sets the track, not the skill.** Piety almost always pays Divinity (80% of Piety successes). Beyond that, the track follows what the knight *did*. Cunning used to trick a tyrant pays Divinity. Cunning used to cheat at dice pays Villainy. A charge on horseback for Arthur pays Romance. The same charge for King Lot pays Villainy.

**The choice sets the track before the roll.** Response choices are often built as a renown fork: *help* (Divinity or Romance) against *rob* (Villainy). The player is choosing a track when they choose a deed, and the resolution only decides how well it goes.

**Villainy pays well. That is the temptation.** Across the published book, successes that grant Villainy average **3.3 Destiny and include a treasure 36% of the time**. Divinity and Romance successes average **2.9 Destiny with a treasure 3–9% of the time**. Villainy is a legitimate way to play and win, not a punishment track. When you offer a wicked choice, make it genuinely rewarding, and let the cost show up elsewhere: lost Divinity, a Pursued or Pariah status, a closed door later (see story tokens).

**Gains far outnumber losses** (about 5 to 1). Losses mark moral turning points:
- *Lose 1–2 Ranks of Divinity* when a knight does something base. This is the most common loss.
- *Lose all Ranks of Villainy* is **redemption**: a healing miracle, a true penance.
- *Lose all Ranks of Divinity* is a **fall**: a damning bargain, a sacrilege.
- *Lose 1 Rank of Renown, whichever is highest* is public humiliation.

**Sizes:** 1 rank is standard; 2 ranks is a significant deed; 3 is rare and reserved for defining acts.

### Renown as a check

Some resolutions test renown ranks instead of rolling: *use your ranks in Romance to recount your deeds of love*. There is no die. The knight either has the reputation or doesn't.

- Thresholds run 3–5 ranks. **4 is the most common.**
- Many are graded in three bands: *4 or more*, *2–3*, *0–1*. See passage-shapes.md for the JSON mapping.
- Use them when reputation itself is the key: a queen who will only receive famous lovers, witches who respect only real wickedness, a hermit who can see holiness.
- Villainy checks are as common as Divinity and Romance checks. Wicked knights get their own doors.

### Renown as a modifier

Small conditional add-ons inside a reward bracket, written as reward `notes`:
- *If you are Betrothed, gain 1 Rank of Villainy.* A romance while promised to another is infidelity.
- *If you have 0 Ranks of Divinity, gain 1 Rank of Divinity.* A first step toward grace.
- *Every Knight who is Betrothed and has 0 Ranks of Villainy gains 1 Rank of Romance.* An age-start blessing for the faithful.

The reader can't check these conditions, so the player applies them, just as with the printed book.

### Renown at the table's scale

Renown is also score. Age starts and the epilogue convert renown into Destiny (for example, *score Destiny equal to your highest Rank of Renown*). The epilogue then reads a closing paragraph chosen by **which renown the whole table accumulated most**. So each age should give every player a reason to pursue each track. The published age starts say so explicitly. Each offers three ways to answer the age's crisis, one per track:

| Age | Divinity answer | Romance answer | Villainy answer |
|---|---|---|---|
| Quest of the Holy Grail | seek the Grail's mysteries | protect those you love while the Grail is gone | rejoice that the Grail has left |
| Final Wars of Britain | restore Camelot's glory | preserve the good already achieved | help bring the Round Table down |

Write your own age starts the same way.

## Story tokens

The game ships 30 numbered story tokens. A book uses them to remember specific events, such as a promise, a betrayal or a debt, so that a later encounter can react.

### Tokens with printed notes

Some physical tokens carry a printed note that belongs to the published book's use of them. The components file records the notes: 4, 5, 6, 8, 9, 10, 11 and 21–26. **Players have only these physical tokens**, so:
- **for your own threads, use the tokens with no printed note:** 1, 2, 3, 7, 12–20, 27–30;
- use a noted token only if your use is consistent with its note (for example, token 22 "Lose a Status" as a boon that removes a status).

### How the published book uses tokens

About 30 tokens are awarded and about 45 checks read them, across roughly 70 passages. A typical token links **two to five passages**. The patterns, from most to least common:

**1. The once-only gate.** At the top of an encounter:
> *If you have Story Token #N, turn immediately to [sequel]. Otherwise, gain Story Token #N and continue reading below.*

The first visit plays the encounter and hands out the token. Any later visit, even through a *different* encounter slot that checks the same token, jumps to a sequel. This is how the book builds **recurring characters across encounter slots**: the same knight, once met in the Dwarf block, is met again in a milieu, and the story remembers.

**2. The allegiance marker.** Awarded when a knight takes a side: joins a rebel king, betrays a fellowship, fails someone disastrously. Checked later to **reroute** (*turn to the passage where your old allies recognise you*) or **bar an option** (*the lord you betrayed will not let you ride with his host*). This is the main way consequences outlive an encounter.

**3. Another player's token.** *If another player has Story Token #12, turn immediately to …* The world remembers what someone else did. Use it for events that change the land: a death, a coronation, a curse.

**4. The map objective.** *Place one of your Quest Markers, as well as Story Token #N, on [a named place]. After you have an encounter there, remove them and gain [reward].* This turns a scene into a small errand across the board. The published book reserves tokens 23–26 for this.

**5. The held boon.** The token *is* the reward: *At any time, you may lose this token to remove one unwanted Status*, or a token placed on a status card to mark a lasting gift. Use it for a charm, a favour owed, a companion's special skill.

**6. The obligation loop.** A token that drags the knight back: *on your next turn you cannot move and must return to the passage on this token*. Used for obsessions, such as an endless hunt for a legendary beast. Pair it with the Obsessed status.

**7. The collection.** Several tokens gathered across one location's rooms or trials, with a final passage that reads which ones you hold and routes accordingly.

**8. The redraw.** *If you have Story Token #N, discard this Feature card, draw a new one, and turn to the new encounter.* This stops an encounter from contradicting what already happened, for example meeting again a king you already killed.

**9. The loss.** *Lose Story Token #N, if possible.* A debt is settled, a vow is fulfilled, or a thread is cut.

**10. The option gate.** *If you do not possess Story Token #N, you may use Cunning to…* Past deeds close off approaches.

### Designing token threads

- **Plan them in the book bible before writing.** For each token: what earns it, every passage that checks it, and what the checks do. Keep a table:

  | Token | Meaning | Awarded at | Checked at | Effect |
  |---|---|---|---|---|
  | 14 | met Sir Aldric at a tournament | 2013 | 2312, 2440 | sequel scenes 1976, 2197, 2560 |

- **Every token awarded should be checked at least once**, and every check should have a token that can be earned. The lint script flags awards with no reader.
- **A token is a memory, not a prize.** Don't award one as a consolation. Award it when something happened that the world should remember.
- **The non-token path must be complete.** Players without the token read on normally. The token path is the bonus branch.
- **In `book.json`,** award with `"rewards": { "storyToken": N }`, and check with a passage link in the body: `If you have Story Token #14, turn immediately to [[1976]].` See passage-shapes.md (gate passages).
