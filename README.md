# D&D Encounter Tracker

### Track initiative, characters, monsters, damage, and health from a Dungeon Master screen and a Player's view where health and damage can be masked by the DM
---

## Functionality Outline

* GUI based interface with the ability to define:
    - Players/Characters
    - Monsters
    - Actions (damage or effect based moves)
    - Health
    - Armor Class
* Functionality includes:
    - add/remove players or monsters
    - add/subtract health
    - add/remove status effects (pre-defined)
    - use "actions" during rounds of combat
    - track rounds of combat
    - prompt, collect, and determine intiative order

---

## Project TO DO:


* Create `Agent` class: base class with common properties and functions of Players and Monsters
    * Create `Player` class: inherits Agent
    * Create `Monster` class: inherits Agent
* Create `Action` class: base class with properties and functions that affect Agent and Status Effect
* Create `StatusEffect` class: base class that affects Agent