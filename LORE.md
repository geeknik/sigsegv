# SIGSEGV // THE HEAP LANDS

> Manage a server. Conquer a Lattice. Attain sudo.

SIGSEGV is a text-based cyberpunk heist RPG where you manage a rogue C2 server, recruit operators, and carve a path through a procedurally generated megacorp lattice, one exploit at a time.

You are not the chosen one. You are a persistent process in a hostile runtime. Stay allocated, stay dangerous, and never let the Garbage Collectors catch your PID.

## 0x01 // The Core Fantasy

- Root Access: Build `root@sigsegv` from a disposable script-kiddie outpost into a black-site empire.
- The Job: Take contracts for data theft, sabotage, extraction, assassination, and infiltration.
- The Crew: Recruit street samurai, riggers, deckers, and unstable specialists. Equip them, manage trauma, and send them into the meatspace.
- The Code: Hack systems by writing code in ZIG-0, an in-universe Zig-like language where breaches are logic puzzles instead of dice rolls.

## 0x02 // Key Features

### Text-first, systems-heavy

Graphics are not the point. SIGSEGV is built around a fast, dense terminal UI where the command console replaces the old throne-room loop. The player triages incidents, accepts jobs, manages heat, and responds to dark-net traffic with a keyboard-first workflow.

### Deep hacking mechanics (ZIG-0)

- Use functions, loops, pointers, and logic bombs to bypass security.
- Defensive code fights back through firewalls, ICE, and trace routines.
- Loot snippets from defeated nodes and operators to extend your exploit library.

### Infinite procedural world

- Megacorps are generated with histories, executives, doctrine, and security profiles.
- The Lattice is an expanding graph of hostile and exploitable nodes.
- Narrative systems track behavior, build grudges, and let the net remember your crimes.

### Heat and consequences

- Low Heat: jobs stay clean and markets stay open.
- High Heat: patrols intensify, ICE hardens, and access closes.
- Critical Heat: Garbage Collectors sweep your region and try to terminate your process.

## 0x03 // The Run Loop

1. BOOT: choose origin, constraints, and starting rig.
2. ROOT: resolve console events, packets, crew drama, opportunities, and threats.
3. PLAN: choose the target, approach, crew, and loadout.
4. EXECUTE: tactical text encounters across stealth, social engineering, routing, gunfights, and net-running.
5. EXTRACT: get paid in cycles, data, gear, reputation, and code.

## The Core Dump

### 1. The Genesis: `panic(2038)`

The world did not end in nuclear fire. It ended because global infrastructure ran out of address space.

In 2038, legacy time integers overflowed. The hyper-connected planetary mesh called the Mainframe suffered a catastrophic kernel panic. Critical infrastructure desynchronized. The Real and the Net collapsed into each other and became corrupted runtime debris known as the Heap.

Civilization broke into fragmented memory blocks. Reality is now unmanaged. There is no `free()`. There is only the fight for allocation.

### 2. The Geography: Stack vs. Heap

- The Stack: rigid cities ruled by megacorps, where identity is statically assigned and deviance is treated as a compile-time error.
- The Heap: unstable wasteland full of leaked memory regions, orphaned processes, dangling pointers, and outlaw freedom.

### 3. The Major Powers

#### Runtime Authorities

- Garbage Collectors: hunter-killers who sweep the Heap and terminate orphaned processes.
- Borrow Checkers: a fanatical order obsessed with safety, ownership, and immutable law.

#### The Corrupted

- Null Pointers: nihilist cults worshipping `0x0` and self-erasure.
- Legacy Daemons: ancient sentient software that survived the crash and evolved into local warlords.

## Gameplay Vocabulary

| Standard Term | SIGSEGV Term | Meaning |
| --- | --- | --- |
| Mana | Entropy | Raw chaos needed to bypass security checks. |
| Spell | Payload | Injected code that alters reality. |
| Sword or Gun | Binary | A compiled executable used as a weapon. |
| Potion | Patch | A hotfix for health, state, or code. |
| Soul | PID | The process identity that must survive. |
| Necromancy | Forking | Spawning a child process from a dead entity. |
| Dungeon | Subnet | An isolated hostile cluster with loot and secrets. |

## Procedural Mission Generator

Missions are built by combining `[Actor] + [Action] + [Target] + [Twist]`.

### Sample tables

Actor:

1. A sentient chatbot escaping its training cage.
2. A corrupted crypto-miner hunting a GPU farm.
3. A ghost with a damaged consciousness file.
4. A junior sysadmin who deleted production.

Action:

1. `DUMP` - extract data from a hardened node.
2. `KILL` - terminate a specific PID.
3. `INJECT` - upload malware into critical infrastructure.
4. `DE-ORPHAN` - rescue a child process that lost its parent.

Target:

1. The AWS Jungle.
2. The Blue Screen Desert.
3. The Legacy Bank.

Twist:

1. The client is a honey-pot.
2. The target is your own backup from a previous save.
3. Completion triggers a recursive loop.
4. The reward is encrypted ransomware.

## Example Packet

> **[INCOMING PACKET]**
> **SENDER:** `Unknown<Void*>`
> **SUBJECT:** The Infinite Loop
>
> "Root user, I require assistance. My master, a Legacy Daemon known as 'Clippy', has entered an infinite loop of helpfulness. He is currently consuming 99% of the local CPU trying to format a document that no longer exists.
>
> Objective: inject a `break;` command into his logic center.
> Risk: high. He is guarded by aggressive Spell-Checkers.
> Reward: 500 cycles and a rare `.docx` artifact."

## Artifacts

- The Mechanical Keyboard of Loud Typing.
- The 10GB Ethernet Cable.
- The Floppy Disk of Doom.
- The Unclosed Bracket `}`.

## End Game: `sudo`

Legend says INIT, PID 1, still exists at the center of the Lattice.

Reach it, take control, and you can rewrite the kernel parameters of reality.

Or execute `rm -rf /` and end the world for everyone.
