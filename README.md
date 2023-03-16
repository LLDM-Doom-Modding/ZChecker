# ZChecker

A universal debugger and actors card-index assistant for G-/Q-/LZDoom written in ZScript.

Separated into three large, interdependent parts:

### 1. Console commands (CCMDs)

The main control tool in the game world. All console commands begin with the prefix "zc," so you can type "zc`<tab>`" to show them all. The most commonly used ones are:

- `zchelp [<command>|all]`. Prints a ZChecker help text:
  
  - No arguments: Prints a short ZChecker help text
  
  - `all`: Prints the full help text
  
  - If the argument is a `<command>`: Prints a large help text with examples. Command names can be written without the "zc" prefix: for example, both `zchelp zcadd` and `zchelp add` are valid.

- `zcadd [self|weap] [<pos>]`. Adds the linetarget actor, or the `self.player` pointer, or the currently selected weapon to the info panel at poisition `<pos>` (see [Section 2. Information panels](#2-informational-panels-infopanels)). If the position is omitted, adds to the first empty panel.

- `zcrem [<pos>]` or `zcclear [<pos>]`. Removes an actor from infopanel `<pos>`, or clears all if argument is omitted.

- `zcsummon <actor> [<amount>] [<extra_param[:value]>][,...]`. A powerful extension over the built-in "summon" command. Supports wildcards (e.g. "z*man" for "Zombieman"), has a plethora of parameters, such as spawn amount, spawnhealth, or forcibly disabled infighting.

- `zcsetprop [<pos>] [add|rel[:<srcpos>]|raw] <property[:value]>[,...]`. Sets a property value (including position, certain pointers and common properties like health) for the actor `<pos>`. May be either assigned, or, when possible, added to the current actor's values, or assigned as a sum with the current value from the actor `<srcpos>` (which, by default, is the player actor).

- `zcsetf [<pos>] <flagname> [<value>]`. Toggles, sets or resets the specified flag on the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcsetst [<pos>] <statename>`. Sets the state on the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcgive [<pos>] <invname> [<amount>]`, `zctake [<pos>] <invname> [<amount>]`. Interacts with the specified actor's inventory, similarly to the built-in `give` and `take` console commands. Also, like `zcsummon`, supports wildcards.

There are many other CCMDs that include a wide range of options of controlling the Actors and Thinkers.

### 2. Information panels (infopanels)

The main supervision and monitoring tool. Up to 3 infopanels can be displayed on the screen at a time. All settings for them can be found in the ZChecker panels menu.

Generally, actors are added to the infopanels via CCMDs like `zcadd`.

### 3. The "Everything" maps

These are test maps that have almost all of the currently loaded actors, including third party loaded modifications. All spawn settings are in the ZChecker "Everything" map menu.

These maps add CCMDs with the "zcev" prefix:

- `zcev recreate` or `zcevre`. Recreates all actors on the Everything map.

- `zcev goto <class>|start` or `zcevg <class>|start`. Teleports the player next to the specified actor or to map start. Wildcards are also recognized.

- `zcev map` or `zcev level`. Warp to the `Everything` map.

- `zcev map2` or `zcev level2`. Warp to the `Everything_simple` map.

Note: the Everything map may be outdated in the beta versions of the project. It's recommended to use `Everything_simple` instead.

## General notes

Wildcards in actor names are `*` (asterisk) and `-` (hyphen). 

`*` may be replaced with any amount (including 0). `-` works the same way but will have at least one character.

Wildcards may be used anywhere and more than once in the mask, so a string like "a-a-a-a" will be parsed as "ArachnotronPlasma", and string "*card" will list all actors whose names end with with "card". To select a specific classname from the list, you can use the `:<index>` or `,<index>` postfixes. For example, "`shot*:2`" will resolve to "Shotgun" (because first element in the list is a "ShotgunGuy" and second is a "Shotgun").

Due to the internal netevent resolution restrictions, you won't be able to provide arbitrary number of space-delimited (" ") arguments for CCMDs. So, if you want to summon a ShotgunGuy that faces away from the player, will not infight others, has a TID of 4, and a great health value, you must specify all of the extra parameters in the comma-separated list: `zcsummon shotgunguy noinfight,relang:180,tid:4,hp:99999`.

---

## Credits

### LLDM crew

- **JSO_x** a.k.a. **Morthimer McMare**: idea, most of the code, the "Everything_simpled" map;

- **StormCatcher.77**: the "Everything" map;

- **ika707**: beta-testing, bug reporting.

### Work with resources

- **Agent_Ash** a.k.a. **Jekyll Grim Payne**: translation check and interface feedback;

- **Dezette** a.k.a. **MyNameIs**: alternative monospaced smallfont;

- **Mud** a.k.a. **Serious_MOod**: textures for the Everything maps.

### Special thanks to

- **Sir Robin**, for his [ZScript quicksort library](https://forum.zdoom.org/viewtopic.php?f=105&t=75757);

- **m8f**, for the GUI code from his [Hellscape Navigator](https://forum.zdoom.org/viewtopic.php?t=61643);

- All beta-testers and critics of ergonomics: **ika707**, **Ron_Dallas**, **Agent_Ash**, **Chameleon_111**, **Il Str**, **Dezette**.
