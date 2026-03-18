# SIGSEGV: The Heap Lands

`SIGSEGV // THE HEAP LANDS`

> Manage a server. Conquer a Lattice. Attain sudo.

SIGSEGV is the new direction for this fork of `usurper-reborn`: a text-first cyberpunk heist RPG about running a rogue C2 node, recruiting operators, and taking contracts across a hostile procedural lattice.

This repository is in transition. The codebase still contains substantial legacy `Usurper Reborn` structures, data, and gameplay systems. The work in this fork is to replace the fantasy/throne-game identity with SIGSEGV's command-console, lattice, crew, and exploit-driven model without lowering the project's security bar.

## Status

- The canonical setting, vocabulary, and core fantasy now live in [LORE.md](/home/geeknik/dev/usurper-reborn/LORE.md).
- Security constraints for the redesign now live in [DOCS/THREAT_MODEL.md](/home/geeknik/dev/usurper-reborn/DOCS/THREAT_MODEL.md).
- Console startup branding now presents the game as `SIGSEGV: The Heap Lands`.
- Most gameplay, localization, web copy, and internal type names are still legacy and will be migrated incrementally.

## Core Fantasy

- Run `root@sigsegv` from a disposable outpost to a black-site empire.
- Take contracts for theft, sabotage, extraction, assassination, and infiltration.
- Recruit street samurai, riggers, deckers, and damaged specialists.
- Break into hostile nodes with code, not abstract dice-roll hacking.
- Manage Heat, survive pursuit, and stay ahead of the Garbage Collectors.

## Design Pillars

- Text-first interface: terminal-native, keyboard-driven, dense, and fast.
- Systems over spectacle: meaningful tradeoffs, layered simulation, procedural factions, persistent consequences.
- Adversarial design: all external inputs are treated as hostile and parser boundaries are explicit.
- Boring security primitives: strict validation, bounded resource usage, minimal trust, least privilege.

## Run Loop

1. `BOOT` - Choose your origin, constraints, and starting rig.
2. `ROOT` - Handle console events, crew drama, offers, threats, and incoming packets.
3. `PLAN` - Pick the target, approach, crew, and payloads.
4. `EXECUTE` - Resolve tactical text encounters in the Net and meatspace.
5. `EXTRACT` - Cash out in cycles, code snippets, gear, and reputation.

## Security Posture

This fork keeps the constraints defined in [AGENTS.md](/home/geeknik/dev/usurper-reborn/AGENTS.md): assume hostile inputs, fail closed, reject unknown fields, avoid dynamic execution, contain privilege boundaries, and prefer proven primitives over cleverness.

Before introducing non-trivial systems such as ZIG-0 scripting, remote mission execution, or new persistence formats, update the trust-boundary analysis in [DOCS/THREAT_MODEL.md](/home/geeknik/dev/usurper-reborn/DOCS/THREAT_MODEL.md).

## Building

Prerequisites:

- [.NET SDK 8.0+](https://dotnet.microsoft.com/download/dotnet/8.0)
- Git

Build and run:

```bash
git clone https://github.com/binary-knight/usurper-reborn.git
cd usurper-reborn
dotnet build usurper-reloaded.csproj -c Release
dotnet run --project usurper-reloaded.csproj -c Release
```

## Project Notes

- Repository path and many internal namespaces still use `usurper-reborn` and `UsurperRemake`.
- Existing BBS, SSH, web, and localization surfaces must be re-themed carefully to avoid user-facing inconsistency.
- The long-term goal is not a cosmetic rename; it is a systemic rewrite around SIGSEGV's setting and mechanics.
