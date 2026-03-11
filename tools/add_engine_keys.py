import json

with open('Localization/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('Localization/es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

new_en = {
    "engine.save_slot_sr_display": "{0}. {1} ({2}) - Level {3} | {4} | {5}",
    "engine.save_slot_level": " - Level {0}",
    "engine.main_title_box": "USURPER REBORN",
    "engine.main_subtitle_box": " - Halls of Avarice",
    "engine.section_play_visual": "  ── PLAY ",
    "engine.section_info_visual": "  ── INFO ",
    "engine.section_accessibility_visual": "  ── ACCESSIBILITY ",
    "engine.bbs_entry_header": "  BBS Name                        Software    Address",
}

new_es = {
    "engine.save_slot_sr_display": "{0}. {1} ({2}) - Nivel {3} | {4} | {5}",
    "engine.save_slot_level": " - Nivel {0}",
    "engine.main_title_box": "USURPER REBORN",
    "engine.main_subtitle_box": " - Salones de la Avaricia",
    "engine.section_play_visual": "  ── JUGAR ",
    "engine.section_info_visual": "  ── INFO ",
    "engine.section_accessibility_visual": "  ── ACCESIBILIDAD ",
    "engine.bbs_entry_header": "  Nombre BBS                      Software    Dirección",
}

for k, v in new_en.items():
    if k not in en:
        en[k] = v
        print(f"  [en] Added: {k}")
    else:
        print(f"  [en] Already exists: {k}")

for k, v in new_es.items():
    if k not in es:
        es[k] = v
        print(f"  [es] Added: {k}")
    else:
        print(f"  [es] Already exists: {k}")

with open('Localization/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, indent=2, ensure_ascii=False)
    f.write('\n')

with open('Localization/es.json', 'w', encoding='utf-8') as f:
    json.dump(es, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("Done! Keys added to en.json and es.json")
