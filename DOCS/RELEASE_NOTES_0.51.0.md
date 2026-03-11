# Usurper Reborn v0.51.0 - "Babel" (Localization Update)

## Localization System

Usurper Reborn now supports multiple languages! The game ships with full English, Spanish, and Italian translations covering 13,589 localization keys — every menu, prompt, combat message, shop interaction, dungeon event, quest, encounter, dialogue choice, and system message in the game. Infrastructure is ready for French, German, Portuguese, and more.

### How It Works

- **Language selection**: Choose `[L] Language` on the main menu before starting, or `[B] Language` in Preferences from any location
- **Per-session in online mode**: Each player can play in their own language simultaneously on the same server (MUD mode uses AsyncLocal per-session)
- **Persistent**: Your language preference saves with your character and restores on login
- **Graceful fallback**: If a translation is missing for your language, the game falls back to English, then to the raw key name — no crashes or blank text

### What's Translated (v0.51.0)

The entire game UI is localized — 13,589 keys covering:

- **All prompts** — "Press Enter to continue..." (441+ instances), "Your choice:" (89+ instances across 28 files)
- **All menus** — Main Street, Inn, Healer, Bank, Temple, Dungeon, Wilderness, Settlement, Castle, Home, Arena, Dark Alley, Love Street, Prison, Music Shop, Weapon Shop, Armor Shop, Magic Shop, Quest Hall, Level Master, Team Corner, Church, and more
- **Combat** — all action labels (Attack, Defend, Power Attack, Precise Strike, Disarm, Taunt, Hide, Flee), combat results, death penalties, victory/defeat messages, monster encounters, spell effects
- **Status displays** — HP, Gold, Mana, Stamina, Level labels in all three display modes (visual, compact/BBS, screen reader)
- **Character system** — all 11 base classes + 5 prestige classes, all 10 playable races, character creation, level-up messages
- **Shops** — buy, sell, pricing, restrictions, inventory displays, equipment stats
- **Dungeon** — floor entry, exploration, traps, treasures, puzzles, riddles, encounters, camping, boss fights
- **Story & quests** — quest descriptions, NPC dialogues, rare encounters, street encounters, companion interactions, Old God encounters, endings
- **System messages** — save/load, time of day, preferences, news, achievements, training, spells

### Languages

| Language | Code | Keys | Status |
|----------|------|------|--------|
| English | en | 13,589 | Base language |
| Spanish (Español) | es | 13,589 | Complete |
| Italian (Italiano) | it | 13,589 | Complete |

### Translation Files

Language files are plain JSON in the `Localization/` directory:
- `en.json` — English (authoritative, 13,589 keys)
- `es.json` — Spanish (complete)
- `it.json` — Italian (complete)

Each file uses flat key-value pairs with `{0}`, `{1}` format placeholders:
```json
{
    "combat.you_hit": "You hit {0} for {1} damage!",
    "combat.you_hit_es": "¡Golpeas a {0} por {1} de daño!"
}
```

### For Translators

To add a new language:
1. Copy `en.json` to `<lang_code>.json` (e.g., `fr.json`)
2. Translate all values (keep keys identical)
3. Keys starting with `_` are comments and ignored
4. The game auto-discovers new language files at startup
5. Pre-registered languages: fr (Français), de (Deutsch), pt (Português), nl (Nederlands), pl (Polski), ru (Русский), ja (日本語), ko (한국어), zh (中文), sv (Svenska), da (Dansk)

### Menu Internationalization

Menu hotkey labels converted from suffix format to full-word format for proper localization. Previously menus used `[D]ungeons` (hotkey letter fused into the word), which broke for non-English languages where the word doesn't start with the hotkey letter. Now uses `[D] Dungeons` / `[D] Mazmorras` / `[D] Sotterranei` — the hotkey stays English while the label is fully translated.

Affects: Main Street menu (17 items), Healer menu (10 items), quick command bar (2 items), Prison menu (1 item).

### Technical Details

- `Loc.Get("key")` — returns localized string for current session language
- `Loc.Get("key", arg1, arg2)` — format string with arguments
- `Loc.Has("key")` — check if a key exists
- Language stored per-character in save data
- `GameConfig.Language` uses `AsyncLocal<string?>` for MUD mode thread safety
- Localization JSON files bundled via .csproj `<Content>` directive

## Bug Fixes

- **Armor shop duplicate Intelligence display** — second `IntelligenceBonus` check replaced with missing `CharismaBonus` in `GetBonusDescription()`
- **Preferences menu case-sensitive** — `switch (choice.Trim())` → `switch (choice.Trim().ToUpperInvariant())`
- **Equipment INT/CON bonuses lost on save/load** — `LootEffects` (canonical storage for Constitution/Intelligence bonuses on inventory items) was never serialized in `InventoryItemData`, causing these stats to silently vanish every save cycle. Also fixed HomeLocation chest storage/retrieval missing LootEffects transfer, and Character `ConvertEquipmentToItem()` missing Charisma bonus.
- **Sage/Magician status spells did nothing** — Freeze, Confusion, Dominate, Poison Touch (Sage) and Sleep, Web, Fear (Magician) all had `if (target != null)` guards that prevented the spell effect from being set, but `target` is always `null` when fighting monsters (combat API passes `null` for monster targets). Removed the guards so spell effects are properly returned to CombatEngine for application.
- **NPC level-up only gained physical stats** — NPCs leveling up via world sim or combat XP only received +STR/+DEF/+HP instead of class-appropriate stat gains (e.g., Magician NPCs had 10 Intelligence at high levels). All 3 NPC level-up code paths now use `LevelMasterLocation.ApplyClassStatIncreases()` for proper per-class stat distribution.
- **Team Corner examine showed incomplete stats** — NPC team member examination only displayed STR/DEF/AGI/STA/WeapPow/ArmPow. Now shows all 7 core stats plus STA/WeapPow/ArmPow.
- **Online mode language selection didn't persist** — `LoadSaveByFileName()` unconditionally overwrote the main menu language choice with the saved language. Fixed with per-session `AsyncLocal<bool>` flag to honor active selection.
- **Home menu ALL CAPS labels** — `home.upgrades` and `home.family` localization keys were in ALL CAPS ("MASTER CRAFTSMAN'S RENOVATIONS", "FAMILY & LOVED ONES") making the menu grid look inconsistent. Changed to title case in both en.json and es.json.
- **World sim catch-up: no cleanup on exception** — `IsCatchUpMode`, `SetActive`, and catch-up buffer were never cleaned up if an exception occurred during catch-up, leaving the world sim in a broken state. Wrapped in try/finally.
- **World sim catch-up: background thread race condition** — Only 100ms wait after `StopSimulation()` before starting catch-up loop; background thread could still be mid-`SimulateStep()`. Increased to 5 seconds.
- **World sim catch-up: off-by-one daily reset** — Loop was `tick < totalTicks` so the final daily reset never fired for 7-day catches. Changed to `tick <= totalTicks`.
- **World sim catch-up: BBS progress bar broken** — `\r` carriage return doesn't work in BBS stdio mode. BBS sessions now use `terminal.WriteLine` with reduced frequency.
- **World sim catch-up: unbounded buffer growth** — Catch-up events list could grow to tens of thousands of entries. Capped at 10,000.
- **World sim catch-up: case-sensitive event categorization** — Keywords like "king" vs "King" were not matched. All categorization now uses case-insensitive comparison.
- **World sim catch-up: emoji TrimStart with multi-byte chars** — `TrimStart('🎂', '💋')` doesn't work with multi-byte Unicode. Replaced with a loop stripping non-letter/digit prefix characters.
- **World sim catch-up: thread-unsafe buffer null check** — `_catchUpBuffer != null` was checked outside the lock in `Newsy()`, creating a race condition with `ClearCatchUpBuffer()`. Moved inside the lock.
- **World sim catch-up: NPC immigration every tick** — `ProcessNPCImmigration()` ran every tick during catch-up instead of being gated by `runVolatileSystems`, causing population explosion. Now gated.
- **World sim catch-up: respawn queue debug log spam** — Respawn queue additions logged on every tick during catch-up, generating thousands of debug entries. Suppressed during catch-up.
- **Old saves trigger full 7-day catch-up on upgrade (CRITICAL)** — Pre-0.51.0 saves have `SaveTime == DateTime.MinValue` (field didn't exist). The catch-up system calculated 2000+ years of absence and ran the maximum 20,160-tick simulation on every first login after upgrading. Now returns early if `SaveTime` is before 2020.
- **Old saves show "0001-01-01" on character selection** — Save slot display showed nonsensical dates for pre-0.51.0 saves. Now hides the "Last played" line for saves without valid timestamps.
- **Missing Localization folder crashes prompts** — BBS sysops who deploy only exe+dll without the `Localization/` folder saw raw key names (e.g., `"ui.your_choice"`) instead of English text. Added built-in English fallback dictionary with ~70 critical UI keys (prompts, status bar, combat actions, equipment slots, save/load messages).

## New Features

### World Sim Catch-Up (Single-Player)

When loading a single-player save after being away, the world now fast-forwards based on your absence duration (up to 7 days / 20,160 simulation ticks). NPCs continue their lives — marriages, births, deaths, level-ups, affairs, settlement building, and political events all play out while you're gone.

- **Progress bar** shows simulation progress during catch-up
- **Narrative summary** categorizes events into Deaths & Departures, Births & Coming of Age, Royal Affairs, Love & Scandal, The Outskirts, and World Events
- **Minimum 10 minutes** absence required before catch-up triggers
- **Screen reader compatible** — text-only progress updates
- Online mode unaffected (already has 24/7 world sim)

## Files Changed

- `Scripts/Core/GameConfig.cs` — Version 0.51.0; `Language` AsyncLocal property (per-session for MUD mode)
- `Scripts/Core/Character.cs` — `Language` property on character for save persistence
- `Scripts/Systems/LocalizationSystem.cs` — **NEW** — `Loc` static class with `Get()`, `Has()`, `GetLanguageName()`, `GetNextLanguage()`; JSON loader with fallback chain; comment key filtering
- `Localization/en.json` — **NEW** — 13,589 English localization keys covering entire game
- `Localization/es.json` — **NEW** — Complete Spanish translation (13,589 keys)
- `Localization/it.json` — **NEW** — Complete Italian translation (13,589 keys)
- `Console/Bootstrap/Program.cs` — `Loc.Initialize()` call at startup
- `usurper-reloaded.csproj` — Localization JSON files as Content (copied to output); IL trimming disabled (was stripping `Path.GetExtension()` and `DbConnection.OpenAsync()` at runtime)
- `Scripts/UI/TerminalEmulator.cs` — `PressAnyKey()` auto-localizes default message; `GetInput("Your choice:")` localized
- `Scripts/Locations/BaseLocation.cs` — `GetChoice()` helper method; language preference toggle `[B]` in preferences menu; all `GetInput("Your choice:")` calls converted; status line HP/Gold/Mana/Stamina/Level labels localized (both visual and compact/BBS modes); screen reader status line localized; inline hint code updated for full-word suffix format
- `Scripts/Locations/MainStreetLocation.cs` — Screen reader menu labels localized (locations, shops, services, status, quit, help)
- `Scripts/Systems/CombatEngine.cs` — Combat action menu labels localized (Attack, Defend, Power Attack, Precise Strike, Disarm, Taunt, Hide, Flee) in both visual and SR modes; `GetInput("Your choice:")` converted; death penalty messages localized (XP loss, gold loss, resurrection)
- `Scripts/Systems/SaveDataStructures.cs` — `Language` field in PlayerData; `LootEffects` field and `LootEffectData` class in `InventoryItemData`
- `Scripts/Systems/SaveSystem.cs` — Language serialization/restore; LootEffects serialization for inventory and chest items
- `Scripts/Core/GameEngine.cs` — Language restore on load; language set on character creation; `GetInput("Your choice:")` converted; save/load messages localized; `[L] Language` on main menu; inventory/chest LootEffects deserialization fix; `[G] Language` in online mode menu; NPC level-up fix (uses `ApplyClassStatIncreases`); world sim catch-up (`RunWorldSimCatchUp`, `ShowCatchUpSummary`, `ShowCatchUpCategory`)
- `Scripts/Locations/DungeonLocation.cs` — `GetChoice()` conversion; floor entry and BBS header localized
- `Scripts/Locations/ArmorShopLocation.cs` — `GetChoice()` conversion; **BUG FIX**: duplicate Intelligence bonus → CharismaBonus fix
- `Scripts/Locations/DevMenuLocation.cs` — Save message localized
- `Scripts/Locations/InnLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/MusicShopLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/DarkAlleyLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/LevelMasterLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/SettlementLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/WildernessLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/LoveCornerLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/QuestHallLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/WeaponShopLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/TempleLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/HomeLocation.cs` — `GetChoice()` conversion; LootEffects transfer in chest equip/store
- `Scripts/Core/Character.cs` — `Language` property; `ConvertEquipmentToItem()` missing Charisma bonus fix
- `Scripts/Core/GameConfig.cs` — World sim catch-up constants (`CatchUpMinAbsenceMinutes`, `CatchUpMaxTicks`, `CatchUpTicksPerDay`, `CatchUpProgressInterval`, `CatchUpMaxEventsPerCategory`, `CatchUpMaxDays`)
- `Scripts/Systems/SpellSystem.cs` — Removed `if (target != null)` guards from 7 debuff spells (Magician: Sleep/Web/Fear; Sage: Poison Touch/Freeze/Confusion/Dominate) so effects work in monster combat
- `Scripts/Systems/WorldSimulator.cs` — `IsCatchUpMode` flag; skip player reputation spread during catch-up
- `Scripts/Systems/DailySystemManager.cs` — `RunCatchUpDailyReset()` lightweight daily reset for catch-up mode
- `Scripts/Systems/NewsSystem.cs` — Catch-up buffer (`SetCatchUpBuffer`/`ClearCatchUpBuffer`); `Newsy()` routes to buffer during catch-up
- `Scripts/Systems/CombatEngine.cs` — NPC combat XP level-up fix (2 paths now use `ApplyClassStatIncreases`)
- `Scripts/Locations/TeamCornerLocation.cs` — Full 7-stat display in ExamineMember (was only STR/DEF/AGI/STA)
- `Scripts/Locations/CastleLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/PrisonLocation.cs` — `GetChoice()` conversion
- `Scripts/Locations/HealerLocation.cs` — `GetChoice()` conversion
- `Scripts/Systems/VisualNovelDialogueSystem.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Systems/RareEncounters.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Systems/CharacterCreationSystem.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Systems/MailSystem.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Systems/InventorySystem.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Systems/DialogueSystem.cs` — `Loc.Get("ui.your_choice")` conversion
- `Scripts/Data/SecretBosses.cs` — `Loc.Get("ui.your_choice")` conversion
