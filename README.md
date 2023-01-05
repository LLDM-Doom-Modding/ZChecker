# ZChecker

A G-/Q-/LZDoom universal debugger and actors card-index assistant written on ZScript.

Separated to three interdependent large parts:

### 1. Console commands (CCMDs)

The main control tool in the game world. All of them are started with the prefix "zc", so you can input a "zc`<tab>`" to show tham all. Most used are:

- `zchelp [<command>|all]`. Prints a short ZChecker help if no arguments provided, full help if there's a keyword "all" and a large help with examples if argument is a `<command>`. You may write command names without a "zc" prefix: for example, both "`zchelp zcadd`" and "`zchelp add`" are valid.

- `zcadd [self|weap] [<pos>]`. Adds a linetarget or a self player or a weapon in hands to the informational panel in position `<pos>` (see [section 2. Informational panels](#2-informational-panels-infopanels)) or to the first empty infopanel if omitted. 

- `zcrem [<pos>]` or `zcclear [<pos>]`. Removes an actor from the infopanel `<pos>` or clears all if argument is omitted.

- `zcsummon <actor> [<amount>] [<extra_param[:value]>][,...]`. A powerful replacement of the built-in "summon" command. Recognizes wildcards ("z*man" for "Zombieman"), has a plethora of parameters such as spawn amount or a start health.

- `zcsetf [<pos>] <flagname> [<value>]`. Toggles, sets or resets a flag for the specified actor (or for the linetarget if omitted).

- `zcsetst [<pos>] <statename>`. Sets a state for the specified actor (or for the linetarget if omitted).

- _`zcsetp [<pos>] <property[:value]>[,...]`_ [WIP]. Sets a property value.

- `zcgive [<pos>] <invname> [<amount>]`, `zctake [<pos>] <invname> [<amount>]`. Operates on the spefified actor's inventory, almost like the built-in "`give`" and "`take`" commands. Like `zcsummon`, recognizes wildcards.

There's many other CCMDs that includes wide range of options to control the Actors and Thinkers.


### 2. Informational panels (infopanels)

The main supervisioning and monitoring tool, up to three infopanels on the screen. All options are in the ZChecker panels menu.

In general, you may add actors to the infopanels via any of the "`zcadd`" commands.


### 3. The "Everything" levels

Has almost all actors in the game, including third party loaded modifications. All spawn options are in the ZChecker "Everything" map menu.

Adds some `zcev`-prefixed commands:

- `zcev recreate` or `zcevre`. Recreates the Everything map.

- `zcev goto` or `zcevg`. Teleports a player's next to the specified actor. Wildcards are also will be recognized.

- ...And some other CCMDs.


## Some remarks

Wildcards in actor names are symbols "`*`" and "`-`". First of them may be replaced with any amount of characters including zero; second will have at least one character. Wildcards may be used anywhere and more than one times in the mask, so string "`a-a-a-a`" will be unparsed to the "ArachnotronPlasma", and string "`*card`" will list all actors which ends with a "card". To specify some classname from the list, you may use a "`:<index>`" or similar "`,<index>`" postfixes. For example, "`shot*:2`" will be unparsed to "Shotgun" (because first element in a list is a "ShotgunGuy" and second is a "Shotgun").

Due to internal netevent realization restrictions you are not able to provide arbitrary number of space-separated ("` `") arguments for CCMDs. So, if you want to summon facing away from the player ShotgunGuy which will not infight others, has a TID of 4 and a great health value, you're must specify all of the extra parameters in the comma-separated ("`,`") list: "`zcsummon shotgunguy noinfight,relang:180,tid:4,hp:99999`".



<p><br></p>

---
## Credits ##

### LLDM crew

- **JSO_x** a.k.a. **Morthimer McMare**: idea, most of the code, map "Everything_simpled";
- **StormCatcher.77**: map "Everything";
- **ika707**: beta-testing, bugs reporting.

### Special thanks to

- **Dezette** a.k.a. **MyNameIs** for the alternative monospaced smallfont.
- Everyone who reports bugs: **ika707**, **Il Str**;
- All beta-testers and critics of ergonomics: **ika707**, **Il Str**, **Ron_Dallas**, **Chameleon_111**, **Dezette**.

### Resources from

- **Sir Robin**, for his ZScript quicksort library: https://forum.zdoom.org/viewtopic.php?f=105&t=75757.
