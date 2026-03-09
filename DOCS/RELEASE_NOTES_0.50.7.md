# Usurper Reborn v0.50.7 — Loot Variety, Prestige Fixes & Ally Combat Buffs

Comprehensive loot template expansion so all classes see diverse weapon and armor drops, buff spells now properly apply to NPC allies, prestige classes bypass all equipment restrictions, god worship persistence fixed for online mode, and font selection available from main menu.

## New Features

### Font Selection on Main Menu
When running in WezTerm (Steam/desktop), the `[F] Terminal Font` option now appears on the main game menu before entering single-player or online mode. Previously font selection was only available in the in-game Preferences menu, which meant online players had to start a single-player game first just to change their font.

### Prestige Classes on Website
All 5 prestige classes (Tidesworn, Wavecaller, Cyclebreaker, Abysswarden, Voidreaver) now appear on the usurper-reborn.net landing page in a dedicated "Prestige Classes (NG+ only)" section with purple accent styling, role descriptions, unlock requirements, and stat bars.

## Bug Fixes

### Prestige Classes Blocked from Equipment
Prestige classes (Tidesworn, Wavecaller, Cyclebreaker, Abysswarden, Voidreaver) were blocked from buying or equipping class-restricted gear. While dungeon loot generation already had a prestige bypass, three other systems did not:

- **`CanEquip()` method** — The core equipment check rejected prestige classes from all class-restricted items. Now bypasses both class restrictions and armor weight restrictions for prestige classes.
- **Weapon Shop** — Display dimmed class-restricted items and purchase validation blocked prestige buyers. Both fixed.
- **Armor Shop** — Same display and purchase blocks. Both fixed.

Prestige classes can now use any weapon and wear any armor regardless of class or weight restrictions.

### God Worship Reverting to Manwe on Login (Online)
Players reported their god worship reverting to "Manwe" (the Supreme Creator / final boss) every time they logged in. Two root causes:

- **Manwe was worshippable at the Temple** — The god selection list included Manwe (Supreme Creator, a system god) alongside the normal pantheon gods. Players could accidentally worship Manwe. Now filtered out of all temple god selection lists.
- **Stale god snapshots in online mode** — Each player's save captured the entire `playerGods` dictionary (all players' worship choices). On login, `RestoreStorySystems` replayed ALL entries, overwriting other players' current worship with stale data from this player's last save. Now only restores the current player's own god entry in online mode.
- **Login cleanup** — Any player with Manwe stored as their elder god gets it auto-cleared on login.

### Buff Spells Ignored on NPC Allies
When casting buff spells (Time Stop, protection spells, etc.) on NPC teammates or companions, the effects were applied to the character's stats but **never checked during monster attacks**:

- **Dodge ignored** — `DodgeNextAttack` (from Time Stop, evasion abilities, etc.) was only checked for the player, never for companions/NPCs. Monsters always hit allies regardless of dodge buffs.
- **Protection/defense buffs ignored** — `MagicACBonus` (from protection spells) and `TempDefenseBonus` (from Time Stop, buff abilities) were never added to companion defense calculations. Ally-targeted protection spells had zero combat effect.

Both are now checked in `MonsterAttacksCompanion()`.

### Loot Drop Variety — All Classes
Players reported only seeing bows, staves, and shields as dungeon loot. Root cause: the only "All"-class weapon templates above level 30 were 10 bows. Non-martial classes (Magician, Sage, Bard, Jester, Alchemist, Cleric) had extremely limited weapon pools dominated by bows.

**Weapons**: 6 new "All"-class general weapons covering levels 25-100 (Fine Dagger, Soldier's Sword, Forged Mace, Tempered Blade, Runed Sword, Ancient Blade). Long Sword changed from Warrior-restricted to All.

**Body armor**: 5 new "All"-class templates covering levels 25-100 (Reinforced Leather, Chainweave Tunic, Forged Brigandine, Runed Hauberk, Ancient Mail). Previously had zero "All" body armor above level 30.

**Per-slot armor** (head, arms, hands, legs, feet, waist, face, cloak): 2-3 new "All"-class templates per slot filling the gap between low-level items (1-30) and Mithril (50-90) — Reinforced (20-50), Forged (35-70), and Runed (65-100) tiers.

**Shields**: Steel Buckler changed to "All", plus 3 new "All" shields (Reinforced Shield, Forged Shield, Runed Shield).

This ensures every class at every level has meaningful loot variety across all equipment slots — important for equipping NPC teammates and companions too.

### Screen Reader Launcher Error Suppressed
`Play-Accessible.bat` (Steam screen reader launcher) showed a "'mode' is not recognized" error on some Windows environments where the `mode` console command isn't on PATH. Error now suppressed with `2>nul` so screen readers don't read it.

## Files Changed
- `Scripts/Core/GameConfig.cs` — Version 0.50.7
- `Scripts/Core/GameEngine.cs` — `[F] Terminal Font` option in main menu (WezTerm only); font cycle handler; Manwe worship cleanup on login; online-mode god restore filter; dual-worship cleanup refactor
- `Scripts/Core/Items.cs` — `CanEquip()` bypasses class restrictions and armor weight restrictions for prestige classes
- `Scripts/Locations/BaseLocation.cs` — `IsRunningInWezTerm()`, `ReadCurrentFont()`, `WriteTerminalFont()` changed from `private` to `internal` for main menu access
- `Scripts/Locations/WeaponShopLocation.cs` — Prestige class bypass for shop display and purchase class restriction checks
- `Scripts/Locations/ArmorShopLocation.cs` — Prestige class bypass for shop display and purchase class restriction checks
- `Scripts/Locations/TempleLocation.cs` — Manwe (Supreme Creator) filtered out of temple god selection lists
- `Scripts/Systems/CombatEngine.cs` — `MonsterAttacksCompanion()` now checks `DodgeNextAttack`, `MagicACBonus`, and `TempDefenseBonus`
- `Scripts/Systems/LootGenerator.cs` — 6 new "All" weapon templates; 5 new "All" body armor templates; 2-3 new "All" templates per armor slot (head, arms, hands, legs, feet, waist, face, cloak); 3 new "All" shields; `TwoHandedWeaponStartIndex` updated from 55 to 61
- `Scripts/Systems/SaveSystem.cs` — `RestoreStorySystems()` accepts optional `onlyRestoreGodForPlayer` parameter; online mode filters god restoration to current player only
- `launchers/Play-Accessible.bat` — Suppressed `mode con:` error with `2>nul`
- `web/index.html` — Added 5 prestige classes to Classes section with purple accent styling
