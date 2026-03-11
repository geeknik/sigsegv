"""
Fix key Spanish prompts/labels that are still in English.
These are player-facing interactive prompts that should be translated.
"""
import json

es_translations = {
    # Interactive prompts still in English
    "street.merchant_buy_prompt": "Comprar cual articulo? ",
    "street.murder_revenge_prompt": "\n  Tu respuesta? ",
    "street.throne_prompt": "\n  Tu decreto, Majestad? ",
    "inn.high_low_prompt": "Mayor (H) o Menor (L)? ",
    "inn.skull_hit_or_stand": "Pedir (H) o Plantarse (S)? ",
    "base.talk_to_who": "Hablar con quien? ",
    "dungeon.fallen_adventurer_choice": "(B)uscar sus pertenencias o (R)espetar a los muertos? ",
    "dungeon.portal_choice": "(E)ntrar al portal, e(S)tudiarlo, o (I)gnorarlo? ",
    "dungeon.duelist_choice": "(A)ceptar el desafio, (D)eclinar cortesmente, o (I)nsultarlos? ",
    "dungeon.treasure_chest_choice": "(A)brir el cofre o (D)ejarlo? ",
    "dungeon.strangers_choice": "(P)elear, pa(G)arles, o intentar (E)scapar? ",
    "dungeon.damsel_choice": "a(Y)udarla, (I)gnorar la situacion, o (U)nirse a los rufianes? ",
    "dungeon.wounded_choice": "a(Y)udarlo, (R)obarlo, o (D)ejarlo? ",
    "dungeon.shrine_choice": "(R)ezar en el santuario, (P)rofanarlo, o (D)ejarlo? ",

    # Castle menu options still in English
    "castle.gift_spouse_option": "]egalo al conyugue (mejorar felicidad)",
    "castle.divorce_option": "]ivorcio (consecuencias politicas)",
    "castle.return_option": "]egresar",
    "castle.designate_heir_option": "]esignar un heredero",
    "castle.name_heir_option": "]ombrar nuevo heredero (adoptar/legitimar)",
}

path = 'Localization/es.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixed = 0
for key, value in es_translations.items():
    if key in data and data[key] != value:
        data[key] = value
        fixed += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"es.json: translated {fixed} English prompts to Spanish")
