# Checks and rewards

How the published book chooses skills, sets targets, and sizes success and failure. The figures come from roughly 780 success outcomes and 490 failure outcomes in the book. Story tokens and renown have their own file: story-tokens-and-renown.md.

## Choosing the skill

Choose the skill from the **deed**, not from the character. The book keeps the twelve skills evenly used: each appears in 55–70 checks. Across a whole book, aim for the same balance.

| Skill | Category | The deed it tests |
|---|---|---|
| Warfare | Martial | leading troops, a siege, a battle plan, commanding a crew, a melee |
| Sword & Shield | Martial | single combat on foot, disarming, breaking a door or a guard |
| Mounted | Martial | a joust, a charge, riding hard to arrive in time, fighting from the saddle |
| Piety | Spiritual | prayer, a moral appeal, shaming wrongdoers, healing by faith, laying a spirit to rest |
| Wisdom | Spiritual | knowledge, history, reading a riddle or a dream, seeing through a lie, wise counsel |
| Magic | Spiritual | casting, dispelling, warding, breaking an enchantment, bargaining with the fay |
| Diplomacy | Courtly | persuasion, negotiation, calming a crowd, brokering a peace |
| Cunning | Courtly | tricks, disguise, theft, cheating, a riddle answered cleverly, a trap in words |
| Honor | Courtly | courtesy, keeping one's word, an appeal to someone's honour, graceful conduct, courtship |
| Nature Lore | Wilderness | herbs and remedies, beasts, weather, finding the better path or the softer ground |
| Endure Hardship | Wilderness | digging, holding on, surviving cold or hunger, labour, resisting pain or temptation |
| Hunting | Wilderness | tracking, archery, setting a snare, stalking, infiltration by stealth |

**Two options in one resolution should come from different categories**, or at least be clearly different deeds: force against wit, faith against cunning, horse against foot.

**Category checks** ("1 Martial Skill of your choice") suit deeds any skill in the family could do, such as "help defend the castle". About 45 checks in the book use a category.

**Renown checks** ("your ranks in Villainy") suit deeds that rest on reputation, such as swaying witches with a tale of your wickedness, or recounting your deeds of love. See story-tokens-and-renown.md.

## Setting the target

Targets are per option. The knight rolls a die, adds their skill rank, and must equal or beat the target.

**Fixed targets.** From about 170 legible fixed targets:

| Target | Share | Use for |
|---|---|---|
| 2 | 2% | a trivial or comic task |
| 3 | 16% | easy: the obvious approach to a small problem |
| **4** | **31%** | **standard** |
| **5** | **28%** | **demanding** |
| 6 | 17% | hard: a dangerous or subtle deed |
| 7–8 | 3% | legendary (the Questing Beast is 8) |

**Location-scaled targets** (`{ "base": N, "addLocationNumber": true }`) account for roughly two checks in five, judging by how often the matching reward scales with the Location #. They appear across the whole book, not only in milieus. Bases run 2–5, and **3 is by far the most common**. Use them when the difficulty should depend on how wild or perilous the knight's current space is: travel, wilderness, a fight whose scale depends on where you are.

**Pairing.** A resolution often pairs one fixed-target option with one location-scaled option. That is a good default.

## Success rewards

A success typically grants **three items** (45% of successes). 88% grant between two and four.

| Element | How often | Typical form |
|---|---|---|
| Destiny | 95% | **Location-scaled in about 42%** (`= Location #`, `= 1 + Location #`, `= 2 + Location #`). Otherwise 2 (16%), 3 (15%), 4 (10%), 1 (8%), 5 (3%), 6–7 (rare). |
| Skill of your choice | 74% | one skill from a category, **usually the category of the skill tested** (about 75%). Sometimes a specific named skill, or two. |
| Renown | 69% | 1 rank (most common) or 2 ranks. 3 ranks is exceptional. See below for which track. |
| Status | 31% | positive ones: Accompanied, Esteemed, Determined, Blessed, Beloved, Betrothed. A **cost of success** is also common: Accursed, Wounded, Imprisoned. |
| Treasure | 18% | `1` (a random draw) far more than a named treasure. Named treasures are for climaxes. |
| Story token | 2% | only when a thread begins (see story-tokens-and-renown.md) |

**Location-scaled Destiny goes with location-scaled targets.** When the check scales with the Location #, the reward usually does too. The schema supports `"destiny": "location_number"`. For "1 + Location #", use `location_number` and add `[Gain 1 additional Destiny]` in the body.

**Size by difficulty and consequence, not by length of prose.**

| Encounter weight | Destiny | Other |
|---|---|---|
| Light (target 3, small stakes) | 1–2 | a skill, *or* a rank |
| Standard (target 4–5) | 2–3 or `location_number` | skill of choice **and** 1–2 ranks |
| Major (target 6, or a turning point) | 3–5 | skill of choice, 2 ranks, plus a status or treasure |
| Climax (Place of Power, legendary figure) | 4–6 | two skills, 2–3 ranks, named treasure or Monarch |

## Failure rewards

This is where the published book differs most from the instinct that every outcome should pay.

| Element | How often |
|---|---|
| **Gains a named skill** | **78%** (65%: exactly the skill tested; 13%: a related "lesson" skill) |
| Negative status | ~48% |
| Destiny | **12%**. Most failures grant none. |
| Renown loss | ~9% |
| Villainy gained | ~6% (usually when the knight tried something underhanded and bungled it) |
| Items in total | one item (35%), two items (47%), three or more (18%) |

**The typical failure is `Gain <skill tested>`, often with `Become <status>`.** For example: *Gain Hunting | Become Pursued*, *Gain Cunning | Become Imprisoned*, *Gain Mounted*.

**The lesson skill.** About one failure in six grants a *different* skill: the one the scene actually taught. Losing an argument with a clever abbess teaches Wisdom. A failed attempt to save someone by force teaches Endure Hardship. When you do this, the failure text must end on that lesson (see style-guide.md).

**When failure gives Destiny**, it is because the failure is still an honourable deed that moved the story on, or the passage is a major one. Keep it at 1–2 unless it is a climax.

**For category checks**, the failure gains a skill from that category: `{ "category": "Martial" }`.

**For renown checks**, a failure usually gains a skill that fits the approach, or nothing but a status.

## Negative statuses: which failure earns which

How often each status is gained as a failure consequence in the published book, and what earns it:

| Status | Failures | Earned by |
|---|---|---|
| Wounded | 49 | lost fights, falls, beasts |
| Scorned | 45 | insulting or disappointing someone who matters, especially socially |
| Pursued | 44 | making enemies who will follow: brigands, spirits, a wronged lord |
| Imprisoned | 41 | captured, trapped, arrested |
| Lost | 32 | led astray: fog, faerie paths, a false guide |
| Despairing | 27 | failing someone you tried to save |
| Accursed | 26 | offending the fay, a witch or the dead |
| Enraged | 24 | being made a fool of, or trying and failing through frustration |
| Doomed | 23 | fate itself turning against you, prophecy, grave sacrilege |
| Unhorsed | 20 | a lost joust or charge, a lost mount |
| Beast Form | 19 | fay transformation, a curse, eating or drinking the wrong thing |
| Plague-Ridden | 16 | swamps, filth, sickbeds, corpses |
| Ensorcelled | 16 | falling under a spell |
| Covetous | 15 | being cheated of treasure, or grasping at it |
| Mad | 15 | glimpsing what should not be seen, a fay revel |
| Licentious, Smitten | 9, 8 | romantic failures and seductions |
| Pariah | 11 | betraying one's own side |

Positive statuses (gained mostly on success): **Accompanied** (a companion joins; the most frequent status in the book, 54 awards), **Blessed**, **Esteemed**, **Determined**, **Beloved**, **Betrothed**, **Monarch** (rare, for the greatest deeds).

Statuses can also be **lost** as rewards: `Lose Unhorsed` (given a horse), `Lose Pursued` (enemies shaken off), `Lose Obsessed` (not yet in the components file; see story-tokens-and-renown.md), `Lose Beast Form`, or *remove 1 unwanted Status Card*.

## What statuses do, and why it matters when you write

A summary of the physical status cards, paraphrased from photographs of the cards. Size a status by what it does, not by its name.

**Statuses that force a choice.** A knight holding one of these must take the matching choice whenever a response offers it. So the verbs in your choices matter:

| Status | Must choose any option to… | So write those options with the verbs |
|---|---|---|
| Covetous | steal or rob | *steal*, *rob* |
| Licentious | court or seduce | *court*, *seduce* |
| Enraged | attack, fight or joust | *attack*, *fight*, *joust* |

Name thefts, seductions and fights plainly. A choice worded "relieve him of his purse" lets a Covetous knight dodge the card.

**Statuses that hand choices to another player:** Ensorcelled (another player makes the knight's narrative decisions) and Mad (another player picks which skill or renown the knight uses, and the knight can't stop in a city). Lost lets another player move the knight.

**Dice modifiers:**

| Status | Effect |
|---|---|
| Blessed | roll twice, take the higher. Lost on becoming Accursed. |
| Accursed | roll twice, take the lower. Lost on becoming Blessed. |
| Atoning | roll twice, take the lower. When it expires normally, the knight gains Divinity and sheds Villainy and Pariah. Gaining Villainy ends it badly. |
| Wounded | Martial checks: roll three, take the lowest. Can spend a turn recovering. |
| Beast Form | Martial and Wilderness checks roll twice and take the higher. Courtly checks roll three and take the lowest. |
| Doomed | every roll counts as a 1 |
| Despairing | no skill bonuses on rolls |
| Monarch | on gaining it, +2 ranks of the highest renown. In a city, roll twice and take the higher. Never expires. |

**Renown and Destiny effects:** Scorned (lose 1 rank of the highest renown on gaining it, and gain 1 less Destiny whenever Destiny is gained), Unhorsed (lose 1 rank of the highest renown on gaining it, no Mounted checks, limited movement, ends in a city), Esteemed (+1 renown on each successful check in a city; ends on becoming a Pariah), Determined (+1 extra rank whenever renown is gained), Betrothed (gains Romance; if already betrothed to someone else, gains Villainy, which is why the book adds *If you are Betrothed, gain 1 Rank of Villainy* to new romances).

**Statuses that send the knight to a passage:** Imprisoned (escape at 2537, rescue by another knight at 2544), Pursued (a Wilderness check after moving, or an encounter at 2550), Smitten (a Courtly check each turn: low → Scorned, high → Beloved), Beloved (court → Betrothed, or reject and roll for Scorned, Pursued or Determined), Pariah (a Martial check on entering a city, or become Imprisoned).

**Other:** Accompanied (Skill Markers on the card each add +1 to rolls with that skill; stacks; never expires), Plague-Ridden (movement −1).

So, as a rough scale for failures: **Doomed, Despairing, Accursed and Imprisoned are heavy.** Wounded, Pursued, Scorned, Unhorsed and Lost are moderate. The forced-choice statuses are dramatic rather than costly. Match the weight to the stakes of the scene.

## Movement

- `Move 1 space` (`"movement": 1`) is the standard walk-away reward, and appears about 80 times.
- Longer moves, sea moves, and "move to any City" are rewards for escapes, voyages and magical transport. Write them as bracketed text if they name a place or a mode (see passage-shapes.md).

## Treasures

- A random draw (`"treasures": 1`) accounts for about 90% of treasure rewards.
- Named treasures appear a handful of times each, at the climax of a thread that has been about that object. Use only names from the components file.
- A treasure can be a cost: *Lose 1 Treasure, if possible* when you pay a bribe or a toll.

## Quick templates

```jsonc
// Standard success
{ "destiny": 3, "skills": [{ "category": "Courtly" }], "renown": [{ "type": "Romance", "delta": 1 }] }

// Location-scaled success
{ "destiny": "location_number", "skills": [{ "category": "Wilderness" }], "renown": [{ "type": "Any", "delta": 1 }] }

// Major success
{ "destiny": 4, "skills": [{ "category": "Spiritual" }], "renown": [{ "type": "Divinity", "delta": 2 }], "statuses": [{ "action": "gain", "name": "Blessed" }] }

// Typical failure
{ "skills": [{ "name": "Hunting" }], "statuses": [{ "action": "gain", "name": "Pursued" }] }

// Lesson failure
{ "skills": [{ "name": "Wisdom" }] }

// Walk-away
{ "movement": 1 }
```
