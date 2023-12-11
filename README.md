# ZChecker

A universal debugger and actors card-index tool for G-/Q-/LZDoom written in ZScript. Minimal engine version is **GZDoom 3.3.1**.

### ZChecker postulates (guarantees):
1. No external object can be changed without direct instructions from the user.
2. The stability of the project must be sufficient for it to be included in the permanent autoload list.
3. The speed of the game with the tools should be close to the speed of the game without it.

Video: (a video will be here).



<p><br></p>

The entire project visible to the user is separated into three large, almost independent parts:

### 1. Information panels (infopanels)

The main supervision and monitoring tool. Up to 3 infopanels can be displayed on the screen at a time. All settings for them can be found in the ZChecker panels menu.

Generally, actors are added to the infopanels via CCMDs like `zcadd`.

[<img alt="3 informational panels" src="https://cdn.discordapp.com/attachments/909139474238308353/1129073425655267420/0beefe9b01a4989a.png" width=384/>](https://cdn.discordapp.com/attachments/909139474238308353/1129073425655267420/0beefe9b01a4989a.png)
[<img alt="Lithium" src="https://cdn.discordapp.com/attachments/909139474238308353/1129073425957269554/01e10dd979d123e3.png" width=384/>](https://cdn.discordapp.com/attachments/909139474238308353/1129073425957269554/01e10dd979d123e3.png)
[<img alt="Shut up and Bleed" src="https://i.imgur.com/Rk492nl.png" width=384/>](https://i.imgur.com/Rk492nl.png)
[<img alt="Golden Souls 2" src="https://cdn.discordapp.com/attachments/909139474238308353/1129073427412697138/ee944a61545efec6.png" width=384/>](https://cdn.discordapp.com/attachments/909139474238308353/1129073427412697138/ee944a61545efec6.png)


### 2. Console commands (CCMDs)

The main control tool in the game world. All console commands begin with the prefix "zc", so you can type "zc`<tab>`" to show them all.

![ZChecker CCMDs](https://github.com/LLDM-Doom-Modding/ZChecker/assets/34414934/bf866924-f1b7-4888-95f6-fca220f5fbad)


The most commonly used ones are:

- `zchelp [<command>|all]`. Prints a ZChecker help text to the console:
  
  - No arguments: Prints a short ZChecker help test;
  
  - `all`: Prints the full help text;
  
  - If the argument is a `<command>`: Prints a large help text with examples. Command names can be written without the "zc" prefix: for example, both `zchelp zcadd` and `zchelp add` are valid.

- `zcadd [self|weap|camera|forced] [<pos>]`. Adds the linetarget actor, or the calling player's actor, or the currently selected weapon to the info panel at poisition `<pos>` (see [Section 1. Information panels](#2-information-panels-infopanels)). If the position is omitted, adds to the first empty panel.

- `zcrem [<pos>]`. Removes an actor from infopanel `<pos>`, or clears all if argument is omitted.

- `zcsummon <actor> [<amount>] [<extra_param[:value]>][,...]`. A powerful extension over the built-in "summon" command. Supports wildcards (e.g. "z*man" for "Zombieman"), has a plethora of parameters, such as spawn amount, spawnhealth, or forcibly disabled infighting.

- `zcsetprop [<pos>] [add|rel[:<srcpos>]] <property[:value]>[,...]`. Sets a property value (including position, certain pointers and common properties like health) for the actor `<pos>`. May be either assigned, or, when possible, added to the current actor's values, or assigned as a sum with the current value from the actor `<srcpos>` (which, by default, is the player actor).

- `zcsetf [<pos>] <flagname> [<value>]`. Toggles, sets or resets the specified flag on the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcsetst [<pos>] <statename>`. Sets the state on the specified actor (or for the linetarget if `<pos>` is omitted).

- `zcgive [<pos>] <invname> [<amount>]`, `zctake [<pos>] <invname> [<amount>]`. Interacts with the specified actor's inventory, similarly to the built-in `give` and `take` console commands. Also, like `zcsummon`, supports wildcards.

There are many other CCMDs that include a wide range of options of controlling the Actors, providing useful information about some rarely- or non-changing datasets, partially controlling instances of the Thinker superclass.

#### General notes for CCMDs

Wildcards in actor class names are `*` (asterisk) and `-` (hyphen).

`*` may be replaced with any amount (including 0). `-` works the same way but will have at least one character.

Wildcards may be used anywhere and more than once in the mask, so a string like "a-a-a-a" will be parsed as "ArachnotronPlasma", and string "*card" will list all actors whose names end with with "card". To select a specific classname from the list, you can use the `:<index>` or `,<index>` postfixes. For example, "`shot*:2`" will resolve to "Shotgun" (because first element in the list is a "ShotgunGuy" and second is a "Shotgun").

Due to the internal netevent resolution restrictions, you won't be able to provide arbitrary number of space-delimited (" ") arguments for CCMDs. So, if you want to summon a ShotgunGuy that faces away from the player, will not infight others, has a TID of 4, and a great health value, you must specify all of the extra parameters in the comma-separated list: `zcsummon shotgunguy noinfight,relang:180,tid:4,hp:99999`.



### 3. The "Everything" maps

These are test maps that have almost all of the currently loaded actors, including third party loaded modifications. All spawn settings are in the ZChecker "Everything" map menu.

[<img alt="Colorful Hell" src="https://cdn.discordapp.com/attachments/909139474238308353/1129074980173394080/7d8bdb9868f16ec7.png" width=384/>](https://cdn.discordapp.com/attachments/909139474238308353/1129074980173394080/7d8bdb9868f16ec7.png)
[<img alt="Golden Souls 2" src="https://cdn.discordapp.com/attachments/909139474238308353/1129074981414899883/b128d2b70876f52c.png" width=384/>](https://cdn.discordapp.com/attachments/909139474238308353/1129074981414899883/b128d2b70876f52c.png)
[<img alt="Aliens: The Ultimate Doom" src="https://github.com/LLDM-Doom-Modding/ZChecker/assets/34414934/fd05f8b8-b1d9-4a2c-8013-a4781ceb855a" width=384/>](https://github.com/LLDM-Doom-Modding/ZChecker/assets/34414934/fd05f8b8-b1d9-4a2c-8013-a4781ceb855a)
[<img alt="Reelism Gold" src="https://github.com/LLDM-Doom-Modding/ZChecker/assets/34414934/e46cdcdf-361b-440d-a090-95c0d72a327c" width=384/>](https://github.com/LLDM-Doom-Modding/ZChecker/assets/34414934/e46cdcdf-361b-440d-a090-95c0d72a327c)


These maps add CCMDs with the "zcev" prefix:

- `zcev recreate` or `zcevre`. Recreates all actors on the Everything map.

- `zcev goto <class>|start` or `zcevg <class>|start`. Teleports the player next to the specified actor or to map start. Wildcards are also recognized.

- `zcev map` or `zcev level`. Warp to the `Everything_simple` map.

- `zcev map2` or `zcev level2`. Warp to the `Everything_alternative` map.

Note: the alternative Everything map may be outdated in the beta versions of the project, so, if you're using one of the default, it's recommended to warp to the `Everything_simple` instead.


<p><br></p>

## Credits

### LLDM crew

- **JSO_x** a.k.a. **Morthimer McMare**: idea, most of the code, the default "Everything_simple" map;
- **StormCatcher.77**: the default "Everything_alternative" map;
- **ika707**: beta-testing, bug reporting.


### Modules/API

- **InfernalSky** a.k.a. **Hizenfort**: player cheats infopanel;
- **N00b2015**: "`zcadd force`" CCMD subcommand fix;
- **Mud** a.k.a. **Serious_MOod**: sound definitions infopanel.


### Work with resources

- **Agent_Ash** a.k.a. **Jekyll Grim Payne**: translation check and interface feedback;
- **Dezette** a.k.a. **MyNameIs**: alternative monospaced smallfont;
- **Mud** a.k.a. **Serious_MOod**: textures for the Everything maps.


### Special thanks to

- **Sir Robin**, for his [ZScript quicksort library](https://forum.zdoom.org/viewtopic.php?f=105&t=75757);
- **m8f**, for the GUI code from his [Hellscape Navigator](https://forum.zdoom.org/viewtopic.php?t=61643);
- **Chameleon_111**, for the video footage.
- **InfernalSky** a.k.a. **Hizenfort**, for the video footage.
- All beta-testers and critics of ergonomics: **ika707**, **Mud**, **Agent_Ash**, **N00b2015**, **Chameleon_111**, **Dron12261**, **Renaul Damek**, **Ron_Dallas**, **Dezette**, **Il Str**.
