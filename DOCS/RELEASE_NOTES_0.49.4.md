# Usurper Reborn v0.49.4 — Beyond the Walls

*The world just got a lot bigger.*

---

## Wilderness Exploration

A new location awaits beyond the city gates. Press `[E]` from Main Street to enter **The Wilderness** — four themed regions to explore, each with unique monsters, discoveries, and encounters.

### Regions

| Direction | Region | Min Level | Theme |
|-----------|--------|-----------|-------|
| North | Whispering Forest | Any | Ancient trees, wolves, bandits, forest trolls |
| East | Iron Mountains | 10 | Jagged peaks, golems, wyverns, ice trolls |
| South | Blackmire Swamp | 20 | Murky bogs, undead, witches, fungal horrors |
| West | Stormbreak Coast | 30 | Shipwrecks, pirates, sea serpents, krakens |

### What You'll Find

Each expedition (up to 4 per day) costs 1 hour of game time and some fatigue. Encounters are randomly rolled:

- **Combat (40%)** — Region-themed monsters via the full combat engine with companions
- **Foraging (25%)** — Herbs, berries, ores, pearls, or nothing. Uses the existing herb system
- **Ruins (15%)** — Abandoned structures to search for treasure (or traps)
- **Travelers (10%)** — Woodcutters, merchants, witches, and sailors who offer trades, lore, or healing
- **Shrines (10%)** — Ancient sites that grant small buffs, XP, or stat boosts

### Discoveries

Each region has hidden locations (caves, groves, temples, lighthouses) that you can stumble upon during exploration. Once found, discoveries are permanently unlocked and can be revisited from the `[D] Discoveries` menu for guaranteed encounters.

### Menu Key Change

`[E]` on Main Street now opens the Wilderness. **Evil Deeds** has moved to the Dark Alley — thematically where dark acts belong.

---

## Dungeon Settlements

Four safe outposts now break the dungeon into distinct regions. When you reach a settlement floor, you'll find a friendly NPC offering services in the depths.

| Floor | Name | NPC | Services |
|-------|------|-----|----------|
| 10 | The Bonewright's Forge | Durgan Bonewright, Dwarven Smith | Healing, Trading, Lore |
| 20 | The Rat King's Market | Nix the Fence, Underground Broker | Trading, Lore |
| 35 | The Hermit's Hollow | Old Maren, Herbalist & Seer | Healing, Trading, Lore |
| 65 | The Last Hearth | Captain Voss, Expedition Commander | Healing, Trading, Lore |

### Settlement Services

- **Heal** — Restore HP and MP for gold (cheaper than the town healer, but less effective). Cures poison too
- **Trade** — Buy potions, herbs, antidotes, and other consumables. Prices scale with your level
- **Lore** — Each NPC has 3-4 unique lore fragments about the surrounding dungeon region. Tracked per-character so you can collect them all over multiple visits

First visit triggers a unique greeting; return visits get a different one. Settlement progress persists across saves.

---

## World News From Distant Lands

The daily news feed now includes 1-2 dispatches from distant regions the player never visits — Ashenmoor, the Northern Reaches, the Iron Coast, Crownhaven, the Sunken Isles, and more. These are pure flavor events across 7 categories (war, trade, plague, discovery, political, disaster, monster sightings) that sell the fiction of a world beyond the town walls.

Notable players may also find themselves referenced in the news — bards singing of your exploits, merchants inspired by your wealth, or kingdoms trembling at your reputation.

---

## Evil Deeds Overhaul

The Dark Alley's Evil Deeds system has been completely rebuilt with 15 lore-rich deeds across 3 progressive tiers, replacing the original placeholder (3 identical options for +10 Darkness).

### Tier 1: Petty Crimes (No requirements)

| Deed | Darkness | Gold | Risk | Notes |
|------|----------|------|------|-------|
| Rob a Beggar | +5 | +15-50 | 5% | Shadows +1 |
| Vandalize a Shrine | +8 | — | 0% | -5 Chivalry, Crown -1 |
| Spread Venomous Rumors | +6 | +10 XP | 10% | Shadows +1 |
| Poison the Well | +10 | costs 25 | 15% | Crown -2 |
| Extort a Shopkeeper | +8 | +50-150 | 10% | — |

### Tier 2: Serious Crimes (Level 5+, Darkness 100+)

| Deed | Darkness | Gold | Risk | Notes |
|------|----------|------|------|-------|
| Desecrate the Dead | +15 | +100-300 (costs 30) | 15% | Fail = cursed, lose 10% HP |
| Arson in the Market | +20 | +25 XP | 20% | Shadows +5, Crown -5, news event |
| Blackmail a Noble | +15 | +200-500 | 20% | Fail = assassin, lose 20% HP |
| Whisper Noctura's Name | +25 | +50 XP | 10% | Requires Noctura encountered or Darkness 300+. If Noctura allied, 0% risk |
| Sabotage Crown Wagons | +18 | +30 XP | 15% | Shadows +8, Crown -8. If Shadows faction, 5% risk & double rep |

### Tier 3: Dark Rituals (Level 15+, Darkness 400+)

| Deed | Darkness | Gold | Risk | Notes |
|------|----------|------|------|-------|
| Blood Offering to Maelketh | +40 | +100 XP | 20% | Costs 15% HP (blood price). Reduced if Maelketh defeated |
| Forge a Dark Pact | +30 | costs 500, +75 XP | 25% | Grants 15% damage buff for 10 combats |
| Invoke Thorgrim's Law | +35 | +80 XP | 15% | Requires Lv20+ or Thorgrim encountered. Crown -5, news event |
| Sacrifice to the Void | +50 | costs 1000, +150 XP | 15% | Grants 1 Awakening Point (once per cycle). Fail = lose 2000g |
| Shatter a Seal Fragment | +60 | +200 XP | 10% | Requires 1+ seal collected. Once per cycle. News event |

Each deed has an atmospheric multi-line description. Failed deeds still cost your daily deed counter. Risk percentage determines chance of failure with unique penalties per deed. Dark Pact buff displays in `/health` and persists across saves.

---

## Bug Fixes & Improvements

- **NPC Spell Proficiency Scaling** — NPCs and companions now scale their skill proficiencies with level (Average at low levels up to Superb at 50+) instead of being stuck at the base default. This makes high-level NPC spellcasters significantly more effective in combat
- **Armor Thematic Bonuses** — Armor pieces now gain stat bonuses matching their name theme. A "Sash of Focus" grants Wisdom + Mana, "Barbarian War Helm" grants Strength + HP, "Shadow Cloak" grants Dexterity + Agility, etc. Eight theme categories ensure armor drops feel meaningfully different
- **Kelmscott Mono Font** — Added as a terminal font option in Settings
- **Terminal Font Option Hidden for Non-WezTerm** — The `[7] Terminal Font` settings option now only appears when running inside WezTerm (detected via `TERM_PROGRAM` env var). SSH, BBS, and other terminal users no longer see an irrelevant option
- **Shop Restrictions Relaxed** — Weapon Shop, Armor Shop, and Magic Shop no longer block purchases based on class, level, or alignment. Items you can't personally equip are added to your inventory instead, so you can buy gear for your companions and NPCs. All items are now visible in shop listings regardless of your level
- **Equip or Inventory Prompt** — After purchasing any equipment, you're now asked `[E]quip now or [I]nventory?` instead of auto-equipping. Cancelling slot selection (weapons) or ring finger selection also sends the item to inventory instead of refunding
- **Auto-Equip Preference** — New `[A] Toggle Auto-Equip` option in Settings/Preferences. When disabled, all shop purchases go straight to inventory — no equip prompt at all. Persists across saves
- **Ring Slot Cancel Fix** — When buying a ring with both finger slots occupied, pressing Enter or `[C]` now properly cancels the purchase and refunds gold instead of silently auto-equipping
- **Quest Turn-In Equipment Fix** — Equipment purchase quests now remove items from inventory first before checking equipped slots. Previously, turning in a quest would unequip your worn gear even if you had a spare copy in inventory
- **Poison Spell Damage Scaling** — Poison tick damage now scales with monster HP (3-5% per tick + level bonus) instead of flat 1d4. Poison Touch and other poison effects are now noticeably impactful at all levels
- **Screen Reader Accessibility** — Inn, Temple, Castle (all submenus), Home, and Preferences screens are now fully screen reader compatible. When Screen Reader Mode is enabled, all box-drawing decorations, color-switching bracket menus, and decorative separator lines are replaced with clean plain text. Menus use "K. Label" format instead of `[K]` color-switched brackets. New shared helpers (`WriteBoxHeader`, `WriteSectionHeader`, `WriteDivider`, `WriteSRMenuOption`) on BaseLocation make future locations easy to make accessible

---

## Files Changed

- `Scripts/Core/GameConfig.cs` — Version 0.49.4; `Wilderness = 504` in GameLocation enum; wilderness constants; evil deed tier constants; Dark Pact buff constants
- `Scripts/Core/Character.cs` — Wilderness/settlement properties; `DarkPactCombats`, `DarkPactDamageBonus`, `HasDarkPactBuff`, `HasShatteredSealFragment`, `HasTouchedTheVoid`; `AutoEquipDisabled` preference
- `Scripts/Core/GameEngine.cs` — Restore wilderness, settlement, Dark Pact, and AutoEquipDisabled state from save data
- `Scripts/Data/DungeonSettlementData.cs` — **NEW** — 4 settlement definitions with NPCs, lore fragments, service configuration
- `Scripts/Data/WildernessData.cs` — **NEW** — 4 region definitions with monster families, foraging tables, discoveries, traveler/ruins/shrine encounters
- `Scripts/Locations/WildernessLocation.cs` — **NEW** — Full location with exploration loop, 5 encounter types, discovery system, both full and compact display modes
- `Scripts/Locations/DungeonLocation.cs` — Settlement encounter handler with heal/trade/lore sub-menus; settlement hint in event display
- `Scripts/Locations/MainStreetLocation.cs` — `[E]` changed from Evil Deeds to Wilderness navigation; updated in all 3 display methods; removed dead Evil Deeds code
- `Scripts/Locations/DarkAlleyLocation.cs` — Evil Deeds overhaul: 15 deeds across 3 tiers (DeedTier enum, EvilDeedDef record, tiered display, success/failure system, faction/news/buff integration)
- `Scripts/Locations/BaseLocation.cs` — Added Kelmscott Mono to terminal font cycle; Dark Pact in active buff display; `[A] Toggle Auto-Equip` in preferences menu; `IsRunningInWezTerm()` detection for font option visibility; screen reader helpers (`WriteBoxHeader`, `WriteSectionHeader`, `WriteDivider`, `WriteThickDivider`, `WriteSRMenuOption`, `IsScreenReader`); SR-compatible Preferences menu
- `Scripts/Locations/InnLocation.cs` — Screen reader compatible: 14 box headers, 14 section headers, dividers, and 3 menu SR branches (main menu, gambling den, drinking game)
- `Scripts/Locations/TempleLocation.cs` — Screen reader compatible: 8 box headers, 12 section headers, divider, and main menu SR branch with all conditional options
- `Scripts/Locations/CastleLocation.cs` — Screen reader compatible: 30 box headers, 17 dividers, 10 section headers, 5 victory/failure banners, and 13 menu SR branches (royal menu, exterior menu, prison, guards, magician, fiscal, orders, orphanage, politics, succession, bodyguards, audience, armory)
- `Scripts/Locations/HomeLocation.cs` — Screen reader compatible: 4 box headers, 15+ section headers, SR-aware menu helpers (WriteMenuOption/WriteMenuNL), upgrade screen, equipment management, and sleep/wait option
- `Scripts/Systems/DungeonGenerator.cs` — `Settlement` added to RoomType and DungeonEventType enums; settlement room injection on floors 10/20/35/65; ConfigureSettlementRooms method
- `Scripts/Systems/LocationManager.cs` — WildernessLocation registered; MainStreet ↔ Wilderness navigation
- `Scripts/Systems/LootGenerator.cs` — `ApplyThematicBonuses()` method adding stat bonuses to armor based on template name keywords (8 theme categories)
- `Scripts/Systems/TrainingSystem.cs` — NPC/companion skill proficiency scaling by level (Average → Superb at 50+)
- `Scripts/Systems/WorldEventSystem.cs` — `GenerateDistantWorldNews()` with 8 named regions, ~50 templates across 7 categories, player-referenced news
- `Scripts/Systems/CombatEngine.cs` — Dark Pact damage buff application (+15% dmg) and per-combat decrement (mirrors God Slayer pattern); poison tick damage scaled to 3-5% monster MaxHP + level bonus
- `Scripts/Systems/QuestSystem.cs` — `RemoveQuestEquipment()` checks inventory before equipped slots so worn gear is preserved
- `Scripts/Systems/SaveDataStructures.cs` — Settlement, wilderness, Dark Pact, and AutoEquipDisabled save fields
- `Scripts/Systems/SaveSystem.cs` — Serialize settlement, wilderness, evil deed tracking, and AutoEquipDisabled state
- `Scripts/Systems/DailySystemManager.cs` — Reset WildernessExplorationsToday on daily reset
- `Scripts/Locations/WeaponShopLocation.cs` — Removed level filter from shop display; class/level/alignment checks converted to warnings with inventory fallback; E/I equip prompt; AutoEquipDisabled bypass
- `Scripts/Locations/ArmorShopLocation.cs` — Removed level filter from shop display; class/level/alignment checks converted to warnings with inventory fallback; E/I equip prompt; AutoEquipDisabled bypass
- `Scripts/Locations/MagicShopLocation.cs` — Level check on accessories converted to warning with inventory fallback; E/I equip prompt; ring slot cancel fix; AutoEquipDisabled bypass
