# ZChecker

A G-/Q-/LZDoom universal debugger and actors card-index assistant written on ZScript.

Separated to three interdependent large parts:

### 1. Console commands (CCMDs)

The main control tool in the game world. All of them are started with the prefix "zc", so you can input a "zc`<tab>`" to show them all. Most used are:

- `zchelp [<command>|all]`. Prints a short ZChecker help if no arguments provided, full help if there's a keyword "all" and a large help with examples if argument is a `<command>`. You may write command names without a "zc" prefix: for example, both "`zchelp zcadd`" and "`zchelp add`" are valid.

- `zcadd [self|weap] [<pos>]`. Adds a linetarget actor/a self player/a weapon in hands to the informational panel in position `<pos>` (see [section 2. Informational panels](#2-informational-panels-infopanels)) or to the first empty infopanel if omitted.

- `zcrem [<pos>]` or `zcclear [<pos>]`. Removes an actor from the infopanel `<pos>` or clears all if argument is omitted.

- `zcsummon <actor> [<amount>] [<extra_param[:value]>][,...]`. A powerful replacement of the built-in "summon" command. Recognizes wildcards ("z*man" for "Zombieman"), has a plethora of parameters such as spawn amount, start health or forced infighting disabling.

- `zcsetprop [<pos>] [add|rel[:<srcpos>]|raw] <property[:value]>[,...]`. Sets a property value (including position, some pointers and common interaction properties like health) for the actor `<pos>`. May be simply assigned or, if possible, added to the current actor value/assigned as sum with the current value from the actor `<srcpos>` (player actor itself by default).

- `zcsetf [<pos>] <flagname> [<value>]`. Toggles, sets or resets a flag for the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcsetst [<pos>] <statename>`. Sets a state for the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcgive [<pos>] <invname> [<amount>]`, `zctake [<pos>] <invname> [<amount>]`. Operates on the specified actor's inventory, almost like the built-in "`give`" and "`take`" commands. Also, like `zcsummon`, recognizes wildcards.

There's many other CCMDs that includes wide range of options of controlling the Actors and Thinkers.


### 2. Informational panels (infopanels)

The main supervisioning and monitoring tool, up to three infopanels on the screen. All settings for them are in the ZChecker panels menu.

Generally, you may add actors to the infopanels via commands of the kind "`zcadd`".


### 3. The "Everything" levels

Has almost all of the currently loaded actors, including third party loaded modifications. All spawn settings are in the ZChecker "Everything" map menu.

Adds some `zcev`-prefixed commands:

- `zcev recreate` or `zcevre`. Recreates all actors on the Everything map.

- `zcev goto <class>|start` or `zcevg <class>|start`. Teleports a player next to the specified actor or to start point. Wildcards are also will be recognized.

- `zcev map` or `zcev level`. Warp to map "`Everything`".

- `zcev map2` or `zcev level2`. Warp to map "`Everything_simple`".

Note: map "`Everything`" may be outdated in the beta versions of the project; so right now it's better to use "`Everything_simple`" instead.


## Some remarks

Wildcards in actor names are symbols "`*`" (an asterisk) and "`-`" (a hyphen). First of them may be replaced with any amount (including zero) of any characters; second symbol works same, but will have at least one character. Wildcards may be used anywhere and more than one times in the mask, so string "`a-a-a-a`" will be unparsed to the "ArachnotronPlasma", and string "`*card`" will list all actors which ends with a "card". To specify some classname from the list, you may use a "`:<index>`" or similar "`,<index>`" postfixes. For example, "`shot*:2`" will be unparsed to "Shotgun" (because first element in a list is a "ShotgunGuy" and second is a "Shotgun").

Due to internal netevent realization restrictions in the engine you are not able to provide arbitrary number of space-separated ("` `") arguments for CCMDs. So, if you want to summon facing away from the player ShotgunGuy which will not infight others, has a TID of 4 and a great health value, you must specify all of the extra parameters in the comma-separated ("`,`") list: "`zcsummon shotgunguy noinfight,relang:180,tid:4,hp:99999`".



<p><br></p>

---
## Credits ##

### LLDM crew

- **JSO_x** a.k.a. **Morthimer McMare**: idea, almost all of the code, map "Everything_simple";

- **StormCatcher.77**: map "Everything";

- **ika707**: beta-testing, bugs reporting.


### Work with resources

- **Agent_Ash** a.k.a. **Jekyll Grim Payne**: translation check and interface advices;

- **Dezette** a.k.a. **MyNameIs**: alternative monospaced smallfont;

- **Mud** a.k.a. **Serious_MOod**: textures for the Everything maps.


### Special thanks to

- **Sir Robin**, for his [ZScript quicksort library](https://forum.zdoom.org/viewtopic.php?f=105&t=75757);

- **m8f**, for the GUI code from his [Hellscape Navigator](https://forum.zdoom.org/viewtopic.php?t=61643);

- All beta-testers and critics of ergonomics: **ika707**, **Ron_Dallas**, **Agent_Ash**, **Chameleon_111**, **Il Str**, **Dezette**.
