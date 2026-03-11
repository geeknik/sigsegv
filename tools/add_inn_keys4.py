import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    "inn.drinking_glugg": "Glugg...",
    "inn.drinking_glugg_end": "Glugg...!",
    "inn.drinking_you_dash": "  You - ",
    "inn.drinking_hooray": "...Hooray! ",
    "inn.drinking_hooray_end": "...Hooray!",
    "inn.return_to_bar": " Return to the bar",
    "inn.loyalty_label": "    Loyalty: ",
    "inn.trust_label": " | Trust: ",
    "inn.active_label": " [ACTIVE]",
    "inn.using_2h_weapon": "(using 2H weapon)",
    "inn.slot_empty": "(empty)",
    "inn.which_hand_pre": "Which hand? [",
    "inn.which_hand_mid": "]ain hand or [",
    "inn.which_hand_post": "]ff hand?",
    "inn.cursed_label": " (CURSED)",
    "inn.no_abilities_yet": "No combat abilities available yet.",
    "inn.all_abilities_enabled": "All abilities enabled!",
    "inn.hl_will_next_be": "Will the next roll be ",
    "inn.hl_igher_or": "igher or ",
    "inn.hl_ower": "ower? ",
}

new_es = {
    "inn.drinking_glugg": "Glug...",
    "inn.drinking_glugg_end": "\u00a1Glug...!",
    "inn.drinking_you_dash": "  T\u00fa - ",
    "inn.drinking_hooray": "\u00a1...Hurra! ",
    "inn.drinking_hooray_end": "\u00a1...Hurra!",
    "inn.return_to_bar": " Volver al bar",
    "inn.loyalty_label": "    Lealtad: ",
    "inn.trust_label": " | Confianza: ",
    "inn.active_label": " [ACTIVO]",
    "inn.using_2h_weapon": "(usando arma 2M)",
    "inn.slot_empty": "(vac\u00edo)",
    "inn.which_hand_pre": "\u00bfQu\u00e9 mano? [",
    "inn.which_hand_mid": "]ano principal o [",
    "inn.which_hand_post": "]tra mano?",
    "inn.cursed_label": " (MALDITO)",
    "inn.no_abilities_yet": "No hay habilidades de combate disponibles a\u00fan.",
    "inn.all_abilities_enabled": "\u00a1Todas las habilidades habilitadas!",
    "inn.hl_will_next_be": "\u00bfLa siguiente tirada ser\u00e1 ",
    "inn.hl_igher_or": "\u00e1s alta o ",
    "inn.hl_ower": "\u00e1s baja? ",
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
