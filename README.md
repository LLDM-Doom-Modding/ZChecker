# ZChecker

A universal debugger and actors card-index assistant for G-/Q-/LZDoom written in ZScript.

Separated into three large, interdependent parts:

### 1. Console commands (CCMDs)

The main control tool in the game world. All console commands start with the prefix "zc," so you can type "zc`<tab>`" to show them all. The most commonly used ones are:

- `zchelp [<command>|all]`. Prints a help text:
  
  - No arguments: Prints a short ZChecker help text 
  
  - `all`: Prints the full help text
  
  - If argument is a `<command>`: Prints a large help text with examples. Command names can be written without the "zc" prefix: for example, both "`zchelp zcadd`" and "`zchelp add`" are valid.

- `zcadd [self|weap] [<pos>]`. Adds a linetarget actor/a self player pointer/a weapon in hands to the informational panel in position `<pos>` (see [section 2. Informational panels](#2-informational-panels-infopanels)), or to the first empty info panel if omitted.

- `zcrem [<pos>]` or `zcclear [<pos>]`. Removes an actor from infopanel `<pos>`, or clears all if argument is omitted.

- `zcsummon <actor> [<amount>] [<extra_param[:value]>][,...]`. A powerful extension over the built-in "summon" command. Supports wildcards (e.g. "z*man" for "Zombieman"), has a plethora of parameters, such as spawn amount, spawn health, or forcibly disabled infighting.

- `zcsetf [<pos>] <flagname> [<value>]`. Toggles, sets or resets the specified flag for the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcsetst [<pos>] <statename>`. Sets a state for the specified actor (or for the linetarget if `<pos>` is omitted).

- _`zcsetp [<pos>] <property[:value]>[,...]`_ [WIP]. Sets the value of the specified property.

- `zcgive [<pos>] <invname> [<amount>]`, `zctake [<pos>] <invname> [<amount>]`. Interacts with the specified actor's inventory, similarly to the build in `give` and `take` console commands. Also, like `zcsummon`, supports wildcards.

There are many other CCMDs that include a wide range of options of controlling the Actors and Thinkers.

### 2. Informational panels (infopanels)

The main supervision and monitoring tool. Up to 3 infopanels can be displayed on the screen at a time. All settings for them can be found in the ZChecker panels menu.

Generally, actors are added to the infopanels via CCMDs like `zcadd`.

### 3. The "Everything" maps

These are test maps that have almost all of the currently loaded actors, including third party loaded modifications. All spawn settings are in the ZChecker "Everything" map menu.

These maps add CCMDs with the "zcev" prefix:

- `zcev recreate` or `zcevre`. Recreates all actors on the Everything map.

- `zcev goto` or `zcevg`. Teleports a player next to the specified actor. Wildcards are recognized.

- ...And some other CCMDs.

Note: the "Everything" map may be outdated in the beta versions of the project. It's better to use "`map everything_simpled`" instead.

## Some remarks

Wildcards in actor names are symbols "`*`" (an asterisk) and "`-`" (a hyphen). First of them may be replaced with any amount (including zero) of any characters; second symbol works same, but will have at least one character. Wildcards may be used anywhere and more than one times in the mask, so string "`a-a-a-a`" will be unparsed to the "ArachnotronPlasma", and string "`*card`" will list all actors which ends with a "card". To specify some classname from the list, you may use a "`:<index>`" or similar "`,<index>`" postfixes. For example, "`shot*:2`" will be unparsed to "Shotgun" (because first element in a list is a "ShotgunGuy" and second is a "Shotgun").

Due to internal netevent realization restrictions in the engine you are not able to provide arbitrary number of space-separated ("` `") arguments for CCMDs. So, if you want to summon facing away from the player ShotgunGuy which will not infight others, has a TID of 4 and a great health value, you must specify all of the extra parameters in the comma-separated ("`,`") list: "`zcsummon shotgunguy noinfight,relang:180,tid:4,hp:99999`".

<p><br></p>

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


