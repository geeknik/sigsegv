# Usurper Reborn v0.49.8 — Bug Fixes & Balance

## Settlement Building Display Fix

Buildings actively under construction now show "In Progress" instead of "Not Started" when they haven't yet reached Foundation tier. The building name also displays in cyan instead of dark gray to indicate active construction.

## God Believers Fix

NPC gods now properly retain their simulated worshipper counts. Previously, when a player worshipped and then unworshipped a god, the believer count would drop to 0 because the random NPC baseline (5-50 believers) was being overwritten by the real disciple count. Gods now track a separate `BaselineBelievers` value that persists independently of player worship actions.

## Desecration Exploit Fix

Altar desecration is now limited to 2 per day with escalating divine punishment. Previously, players could infinitely cycle between sacrificing to an evil god (+1 dark deeds) and desecrating altars (-1 dark deeds) for unlimited XP and Darkness gains with no consequences.

- **First desecration**: 30% chance of divine curse (damage + HP loss)
- **Second desecration**: Guaranteed curse with 3x damage plus permanent loss of a random base stat point
- **Third+ attempts**: Blocked until the next day ("The temple guards are watching you too closely")

---

## Files Changed

- `Scripts/Core/GameConfig.cs` — Version 0.49.8
- `Scripts/Locations/SettlementLocation.cs` — "In Progress" display for active buildings at tier None; cyan color for active construction
- `Scripts/Core/God.cs` — `BaselineBelievers` property; updated AddBeliever/RemoveBeliever to preserve NPC baseline; serialization in ToDictionary/FromDictionary
- `Scripts/Systems/GodSystem.cs` — `InitializeDefaultPantheon` sets both BaselineBelievers and Believers
- `Scripts/Core/Character.cs` — `DesecrationsToday` daily counter property
- `Scripts/Locations/TempleLocation.cs` — Daily desecration limit (2/day); escalating divine punishment with stat loss
- `Scripts/Systems/DailySystemManager.cs` — `DesecrationsToday` reset on new day
- `Scripts/Systems/SaveDataStructures.cs` — `DesecrationsToday` field
- `Scripts/Systems/SaveSystem.cs` — `DesecrationsToday` serialization
- `Scripts/Core/GameEngine.cs` — `DesecrationsToday` restore on load
