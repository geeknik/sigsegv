# Usurper Reborn v0.50.1 — Bug Fixes

Hotfix release addressing a crash, an exploit, and a worship system bug.

## Bug Fixes

### Dungeon Entry Crash (NullReferenceException)
Players with companions would crash when entering the dungeon with "Error loading save: Object reference not set to an instance of an object." The `DungeonLocation.EnterLocation()` override didn't call `base.EnterLocation()`, leaving the base class `terminal` field null. When the screen reader accessibility pass (v0.50.0) added `WriteSectionHeader()` calls to `AddCompanionsToParty()`, these used the null `terminal` field and crashed. Fixed by setting `currentPlayer` and `terminal` at the top of the dungeon's `EnterLocation()` override.

### Dual God Worship
Players could worship both an elder god (e.g., Manwe) and an immortal player-god (e.g., fastfinge) simultaneously. The temple displayed "You worship Manwe" while also showing "Following: fastfinge" in the Ascended Gods section. Additionally, multiple players had "Manwe" (the Old God final boss) stored as their worshipped deity despite Manwe not being a valid pantheon god.

Two fixes applied:
- `GetPlayerGod()` now validates the returned god actually exists in the god system. Invalid entries (like "Manwe") are automatically cleaned up and removed.
- A login-time dual-worship guard detects when both `WorshippedGod` (immortal) and an elder god are set, and clears the immortal worship (elder god takes priority).

### Pit Fighting Gold Exploit
Pit fighting bets had no cap — players could bet their entire gold at up to 3x multiplier with fights that were easy to win, making it a reliable gold farming method. Bet amount is now capped at `level * 500` gold.

### Temple Menu Spacing
`[F]The Faith` was missing a space after the bracket — now displays as `[F] The Faith`.

## Files Changed
- `Scripts/Core/GameConfig.cs` — Version 0.50.1
- `Scripts/Locations/DungeonLocation.cs` — Set `currentPlayer` and `terminal` base class fields at top of `EnterLocation()` override
- `Scripts/Systems/GodSystem.cs` — `GetPlayerGod()` validates god exists in system; auto-removes invalid entries with debug log
- `Scripts/Core/GameEngine.cs` — Login-time dual-worship cleanup guard (elder god + immortal conflict)
- `Scripts/Locations/DarkAlleyLocation.cs` — Pit fighting bet cap (`level * 500`)
- `Scripts/Locations/TempleLocation.cs` — `[F] The Faith` spacing fix
