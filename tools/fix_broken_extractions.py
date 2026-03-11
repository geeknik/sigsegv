"""
Fix localization values that contain raw C# expressions instead of proper {0} placeholders.
These were incorrectly extracted from git diffs by the extraction scripts.
"""
import json

# Fixes: key -> corrected value
# For values with GameConfig constants, resolve to the actual static value.
# For values with C# variable references, convert to {0}, {1} placeholders.
fixes = {
    # Class passives - resolve constants
    "base.buff_arcane_mastery": "  - Arcane Mastery: +15% spell damage",
    "base.buff_potion_mastery": "  - Potion Mastery: +50% healing (potions, herbs, elixirs)",
    "base.buff_tricksters_luck": "  - Trickster's Luck: 20% chance of random bonus",

    # Variables that should be {0}, {1} etc
    "base.more": ", +{0} more",
    "base.unknown_quest": "  \u2022 {0}",
    "base.more_quests": "  ... and {0} more quests.",
    "base.server_time": "  Server Time: {0}",
    "base.experience_label": "  Experience: +{0}",
    "base.standing_decreased": "  Your standing with {0} has decreased! (-50)",
    "base.standing_approves": "  {0} approves! (+10 standing)",
    "base.pref_font_set": "Terminal font set to: {0}",
    "base.attack_looted": "  You loot {0} gold from their body.",
    "base.stat_xp_need_total": " (Need {0} total)",
    "base.pref_auto_heal_toggled": "Auto-heal is now {0}",

    # Castle
    "castle.adopt_orphan": "Adopt new orphan ({0} gold from treasury)",
    "castle.commission_orphan": "Commission orphan (recruit age {0}+, 1,000 gold)",

    # Dungeon - fee/gold related
    "dungeon.need_gold_fee": "You need {0} gold but only have {1}!",
    "dungeon.pay_affordable": "Pay {0} gold for allies you can afford? (Y/N): ",
    "dungeon.paid_gold": "Paid {0} gold.",
    "dungeon.pay_all_allies": "Pay {0} gold to bring your allies? (Y/N): ",
    "dungeon.paid_allies_prepare": "Paid {0} gold. Your allies prepare for the dungeon.",
    "dungeon.remaining_gold": "Remaining gold: {0}",
    "dungeon.boss_bonus_share": "Bonus: {0} gold, {1} XP (your share: {2}g, {3} XP)",
    "dungeon.treasure_your_share": "Your share: {0} gold, {1} XP",
    "dungeon.bonus_xp_share": "  Bonus XP: +{0} (your share: {1})",
    "dungeon.bonus_gold_share": "  Bonus Gold: +{0} (your share: {1})",
    "dungeon.bonus_xp": "  Bonus XP: +{0}",
    "dungeon.bonus_gold": "  Bonus Gold: +{0}",
    "dungeon.fatigue_reduced": "You feel somewhat refreshed. (Fatigue -{0})",
    "dungeon.encounter_group_family": " from the {0} family!",
    "dungeon.chest_your_share": "Your share: {0} gold, {1} XP",
    "dungeon.god_slayer_buff": "  Divine power surges through you! (+20% damage, +10% defense for {0} combats)",

    # Inn
    "inn.seth_earn_reward": "You earn {0} experience and {1} gold.",
    "inn.rest_fatigue_reduced": "A brief rest eases your weariness. (Fatigue -{0})",

    # Inventory
    "inventory.value": "  Value: {0} gold",
    "inventory.requires": "  Requires: {0}",
}

for lang in ['en', 'es']:
    path = f'Localization/{lang}.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    for key, value in fixes.items():
        if key in data:
            old = data[key]
            if old != value:
                data[key] = value
                fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{lang}.json: fixed {fixed} keys")
