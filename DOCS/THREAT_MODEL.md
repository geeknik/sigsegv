# SIGSEGV Threat Model

This document is the baseline threat model for the SIGSEGV remake direction. It exists because the project doctrine requires explicit trust boundaries before non-trivial features ship.

## Scope

This applies to:

- Local console play
- BBS door mode
- SSH and MUD server access
- Web terminal and proxy components
- Save backends and administrative surfaces
- Planned ZIG-0 execution, mission generation, and procedural content systems

## Trust Boundaries

### 1. Player input

All keyboard input, commands, names, save selections, chat messages, BBS drop files, and network-delivered payloads are untrusted.

Implications:

- Parse with explicit schemas or fixed command grammars.
- Reject unknown fields and malformed encodings.
- Bound input size and recursion depth.
- Treat terminal escape sequences as hostile data.

### 2. Network transport

SSH, telnet-style door flows, WebSocket relays, HTTP dashboards, and any future remote APIs cross an untrusted network boundary.

Implications:

- Authenticate explicitly.
- Bind sessions to stable identities.
- Rate-limit connection attempts and expensive actions.
- Do not trust client timing, ordering, or replay resistance by default.

### 3. Persistence

SQLite state, JSON saves, drop files, imported data, and future content packs are untrusted at load time, even if produced locally.

Implications:

- Fail closed on corrupt or unexpected state.
- Avoid unsafe deserialization.
- Validate version migrations explicitly.
- Prevent partial writes and torn save transitions.

### 4. Operator and admin tooling

SysOp consoles, deployment scripts, backup tooling, and server configuration hold elevated privileges.

Implications:

- Separate player and operator privileges.
- Never let player-controlled data select arbitrary file paths or shell commands.
- Avoid string-built command execution.
- Keep secrets out of logs, errors, and repository state.

### 5. Planned ZIG-0 execution

User-authored code is the highest-risk future subsystem. It crosses from content into computation.

Implications:

- No direct execution of host-language code.
- No access to filesystem, process, network, reflection, or unmanaged memory from puzzle runtimes.
- Resource budgets must be explicit: CPU steps, memory, output, recursion, and wall-clock time.
- Puzzle sandboxes must be deterministic and fuzzable.

## Sensitive Assets

- Account credentials and session tokens
- Save integrity and character ownership
- Administrative privileges and SysOp controls
- Server availability and process stability
- Audit logs and operational telemetry
- Future procedural seeds when they gate secret content or anti-cheat checks

## Privilege Levels

- Anonymous remote user
- Authenticated player
- Character owner within an account
- SysOp or administrator
- Host process and deployment environment

Privilege transitions must be explicit and auditable.

## Likely Escalation Paths

- Terminal injection through unescaped player-controlled strings
- Authentication confusion between BBS identity, online identity, and alt-character keys
- Save-file tampering leading to privilege or ownership crossover
- Proxy or relay abuse to reach internal services
- Resource exhaustion through oversized payloads, pathological inputs, or sandbox escape attempts
- Future ZIG-0 runtime escapes into host APIs

## Security Invariants

- Unknown input is rejected, not ignored.
- Parsing and validation happen before state mutation.
- Player data never directly maps to filesystem paths, SQL fragments, or shell arguments.
- External error messages stay generic.
- Logs exclude secrets, raw credentials, and full payload bodies.
- Availability is treated as a security property.

## Immediate Design Guidance

- Keep business logic separate from terminal and network I/O.
- Prefer total functions over ambient mutable state.
- Introduce shared request and save schemas before adding new remote surfaces.
- Gate all future scripting mechanics behind a dedicated sandbox design review.
- Update this document before implementing ZIG-0, crew automation, contract networking, or mod/plugin support.
