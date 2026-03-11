import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    # Court politics
    "castle.court_developing": "(Court members will appear as the kingdom develops)",
    "castle.courtiers_scheming": "* Some courtiers seem to be scheming...",
    "castle.court_menu_visual": "[D]ismiss  [A]rrest Plotter  [B]ribe  [P]romote  [Q]uit",
    "castle.faction_status": "  {0}: {1} ({2}%)",
    "castle.faction_loyal": "Loyal",
    "castle.faction_neutral": "Neutral",
    "castle.faction_hostile": "Hostile",

    # Dismiss
    "castle.court_member_entry": "  {0}. {1} ({2}, {3})",
    "castle.dismissed_from_court": "{0} has been dismissed from the court!",

    # Arrest
    "castle.plot_entry": "  {0}. {1} by {2} (Trial cost: {3}g)",

    # Bribe
    "castle.loyalty_label": "Loyalty: {0}% ",
    "castle.cost_label": "(Cost: {0}g)",
    "castle.bribe_abandoned": "{0} has abandoned their scheming! (+{1} loyalty, -{2}g)",
    "castle.bribe_loyalty_up": "{0}'s loyalty increased to {1}%. (+{2} loyalty, -{3}g)",

    # Promote
    "castle.promote_entry": "  {0}. {1} ({2}, Influence: {3})",
    "castle.promoted": "{0} has been promoted! (+{1} loyalty, +5 influence, -{2}g)",

    # Marriage
    "castle.candidate_entry": "{0} +20 {1} relations",
    "castle.accepts_proposal": "{0} accepts your proposal!",
    "castle.declines_proposal": "{0} politely declines your proposal.",

    # Orphan commission
    "castle.commissioned_guard": "{0} has been commissioned as a Royal Guard!",
    "castle.commissioned_merc": "{0} has been commissioned as a Royal Mercenary ({1})!",
    "castle.released_citizen": "{0} has been released into the world as a citizen!",
    "castle.orphan_adopted": "{0}, a {1}-year-old {2}, has been taken into the Royal Orphanage.",
    "castle.boy": "boy",
    "castle.girl": "girl",

    # Bodyguard list
    "castle.merc_entry": "  {0}. {1} - Level {2} {3} ({4}) - HP: {5}/{6}",
    "castle.merc_level_entry": " - Level {0} {1} ({2})",
    "castle.merc_hp_entry": " - HP: {0}/{1}",
    "castle.hired_bodyguard": "{0} has been hired as your royal bodyguard!",
    "castle.dismiss_merc_entry": "  {0}. {1} (Level {2} {3})",
    "castle.dismissed_merc": "{0} has been dismissed from your service.",

    # Quest bounties
    "castle.reward_label": "    Reward: {0}",
    "castle.comment_label": "    {0}",

    # Throne challenge - solo
    "castle.fight_monster_guard": "=== Fighting Monster Guard: {0} (Level {1}) ===",
    "castle.fight_royal_guard": "=== Fighting Royal Guard: {0} ===",
    "castle.guard_flees": "{0} sees your strength and flees from combat!",
    "castle.guard_strikes": "{0} strikes you for {1} damage! (Your HP: {2})",
    "castle.final_battle": "=== Final Battle: {0} {1} ===",
    "castle.round_label": "--- Round {0} ---",
    "castle.king_strikes": "{0} strikes for {1} damage! (Your HP: {2})",

    # Siege - team member entry
    "castle.siege_member_entry": "  {0} (Lv {1})",

    # Siege - combat
    "castle.siege_monster_blocks": ">>> Monster Guard: {0} (Level {1}) blocks the path! <<<",
    "castle.siege_monster_strikes": "  {0} strikes back for {1}! (Team HP: {2})",
    "castle.siege_monster_defeated": "  {0} has been defeated!",
    "castle.siege_guard_stands": ">>> Royal Guard: {0} (Loyalty: {1}%) stands firm! <<<",
    "castle.siege_guard_surrenders": "  {0} throws down their weapon and surrenders!",
    "castle.siege_guard_fights": "  {0} fights back for {1}! (Team HP: {2})",
    "castle.siege_guard_defeated": "  {0} has been defeated!",

    # Siege - king fight
    "castle.siege_vs": "=== {0} {1} vs {2} ===",
    "castle.siege_king_strikes": "{0} strikes you for {1}! (Your HP: {2})",

    # Crime report
    "castle.darkness_label": " (Darkness: {0})",

    # Heir management
    "castle.heir_designated": "{0} has been officially designated as your heir!",
    "castle.heir_added": "{0} has been added to the line of succession!",

    # Armory gold
    "castle.gold_label": "\n  Gold: {0}",
}

new_es = {
    "castle.court_developing": "(Los miembros de la corte aparecerán a medida que el reino se desarrolle)",
    "castle.courtiers_scheming": "* Algunos cortesanos parecen estar conspirando...",
    "castle.court_menu_visual": "[D]espedir  [A]rrestar  [S]obornar  [P]romover  [Q]Salir",
    "castle.faction_status": "  {0}: {1} ({2}%)",
    "castle.faction_loyal": "Leal",
    "castle.faction_neutral": "Neutral",
    "castle.faction_hostile": "Hostil",

    "castle.court_member_entry": "  {0}. {1} ({2}, {3})",
    "castle.dismissed_from_court": "¡{0} ha sido despedido de la corte!",

    "castle.plot_entry": "  {0}. {1} por {2} (Costo del juicio: {3}g)",

    "castle.loyalty_label": "Lealtad: {0}% ",
    "castle.cost_label": "(Costo: {0}g)",
    "castle.bribe_abandoned": "¡{0} ha abandonado sus intrigas! (+{1} lealtad, -{2}g)",
    "castle.bribe_loyalty_up": "La lealtad de {0} aumentó a {1}%. (+{2} lealtad, -{3}g)",

    "castle.promote_entry": "  {0}. {1} ({2}, Influencia: {3})",
    "castle.promoted": "¡{0} ha sido promovido! (+{1} lealtad, +5 influencia, -{2}g)",

    "castle.candidate_entry": "{0} +20 relaciones {1}",
    "castle.accepts_proposal": "¡{0} acepta tu propuesta!",
    "castle.declines_proposal": "{0} rechaza cortésmente tu propuesta.",

    "castle.commissioned_guard": "¡{0} ha sido comisionado como Guardia Real!",
    "castle.commissioned_merc": "¡{0} ha sido comisionado como Mercenario Real ({1})!",
    "castle.released_citizen": "¡{0} ha sido liberado al mundo como ciudadano!",
    "castle.orphan_adopted": "{0}, un {2} de {1} años, ha sido acogido en el Orfanato Real.",
    "castle.boy": "niño",
    "castle.girl": "niña",

    "castle.merc_entry": "  {0}. {1} - Nivel {2} {3} ({4}) - PV: {5}/{6}",
    "castle.merc_level_entry": " - Nivel {0} {1} ({2})",
    "castle.merc_hp_entry": " - PV: {0}/{1}",
    "castle.hired_bodyguard": "¡{0} ha sido contratado como tu guardaespaldas real!",
    "castle.dismiss_merc_entry": "  {0}. {1} (Nivel {2} {3})",
    "castle.dismissed_merc": "{0} ha sido despedido de tu servicio.",

    "castle.reward_label": "    Recompensa: {0}",
    "castle.comment_label": "    {0}",

    "castle.fight_monster_guard": "=== Luchando contra Guardia Monstruo: {0} (Nivel {1}) ===",
    "castle.fight_royal_guard": "=== Luchando contra Guardia Real: {0} ===",
    "castle.guard_flees": "¡{0} ve tu fuerza y huye del combate!",
    "castle.guard_strikes": "¡{0} te golpea por {1} de daño! (Tu PV: {2})",
    "castle.final_battle": "=== Batalla Final: {0} {1} ===",
    "castle.round_label": "--- Ronda {0} ---",
    "castle.king_strikes": "¡{0} golpea por {1} de daño! (Tu PV: {2})",

    "castle.siege_member_entry": "  {0} (Nv {1})",

    "castle.siege_monster_blocks": ">>> ¡Guardia Monstruo: {0} (Nivel {1}) bloquea el paso! <<<",
    "castle.siege_monster_strikes": "  ¡{0} contraataca por {1}! (PV del equipo: {2})",
    "castle.siege_monster_defeated": "  ¡{0} ha sido derrotado!",
    "castle.siege_guard_stands": ">>> ¡Guardia Real: {0} (Lealtad: {1}%) se mantiene firme! <<<",
    "castle.siege_guard_surrenders": "  ¡{0} arroja su arma y se rinde!",
    "castle.siege_guard_fights": "  ¡{0} contraataca por {1}! (PV del equipo: {2})",
    "castle.siege_guard_defeated": "  ¡{0} ha sido derrotado!",

    "castle.siege_vs": "=== {0} {1} vs {2} ===",
    "castle.siege_king_strikes": "¡{0} te golpea por {1}! (Tu PV: {2})",

    "castle.darkness_label": " (Oscuridad: {0})",

    "castle.heir_designated": "¡{0} ha sido oficialmente designado como tu heredero!",
    "castle.heir_added": "¡{0} ha sido añadido a la línea de sucesión!",

    "castle.gold_label": "\n  Oro: {0}",
}

for k, v in new_en.items():
    en[k] = v
for k, v in new_es.items():
    es[k] = v

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_en)} en keys, {len(new_es)} es keys. en: {len(en)}, es: {len(es)}")
