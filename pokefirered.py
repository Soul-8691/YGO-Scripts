import json
import re
from set_chronology import set_chronology_ocg, set_chronology_tcg

f = open('YGOProDeck_Card_Info.json')
data = json.load(f)
card_info = {}
for card_info_data in data['data']:
    card_info[card_info_data['name']] = card_info_data

pack_types = [
    '+1 Bonus Pack',
    'Advent calendar',
    'Animation Chronicle',
    'Astral Pack',
    'Binder',
    'Book promotion',
    'Booster Pack',
    'Booster Pack Reprint Set',
    'Booster Pack Set',
    'Booster SP',
    'Booster pack',
    'Box set',
    'Bundle',
    'Champion Pack',
    'Collector Box',
    "Collector's Set",
    'Collectors Pack',
    'Core Booster',
    'Deck',
    'Deck-Build Pack',
    'Deluxe Edition',
    'Demo Deck',
    'Demo deck',
    'Duel Terminal',
    'Duelist Pack',
    'Duelist Set',
    'Enhancement Pack',
    'Extra Pack',
    'Film promotion',
    'Game Promotional Set',
    'Gold Series',
    'Guide Promotional Set',
    'Hidden Arsenal',
    'Legendary Collection',
    'Limited Edition',
    'Limited Edition Pack',
    'Lost Art Promotion',
    'Magazine Promotional Set',
    'Magazine promotion',
    'Manga promotion',
    'OTS Tournament Pack',
    'One of a kind',
    'Phantom Rage +1 Bonus Pack',
    'Power-Up Pack',
    'Premium Pack',
    'Promotion Pack',
    'Promotional Set',
    'Promotional card',
    'Promotional cards',
    'Promotional set',
    'Sneak Peek',
    'Special Edition',
    'Speed Duel Booster Pack',
    'Speed Duel Sneak Peek',
    'Speed Duel Starter Deck',
    'Speed Duel Tournament Pack',
    "Speed Duel collector's set",
    'Speed Duel demo deck',
    'Speed Duel magazine promotion',
    'Speed Duel promotional card',
    'Star Pack',
    'Starter Deck',
    'Structure Deck',
    'Super Edition',
    'Tactical-Try Deck',
    'Tin',
    'Tournament Pack',
    'Tournament Prize Cards',
    'Tournament promotion',
    'Tournament promotional card',
    'Tournament promotional set',
    'Turbo Pack',
    'V Jump Edition',
    'Value Box',
    'Vendor Edition',
    'Video Game Promotional Card Set',
    'Video Game promotion',
    'Video game promotion'
]

output = open('output.c', 'w', encoding='utf8')

# count = 0
# for race in sorted(list(set(['TYPE_' + re.sub(r'\W+', '_', card_info[card]['type'].replace(" Monster", "").replace(" Card", "")).upper() for card in card_info]))):
#     print('#define ' + race + ' ' + str(count))
#     count += 1

# count = 1
# attributes = list()
# for card in card_info:
#     try:
#         attributes.append('ATTRIBUTE_' + card_info[card]['attribute'].upper())
#     except:
#         pass

# for attribute in sorted(list(set(attribute for attribute in attributes))):
#     print('#define ' + attribute + ' ' + str(count))
#     count += 1

for card in card_info:
    output.write("\t[" + re.sub(r'\W+', '_', card_info[card]['name']).upper() + "] =\n"
                 + "\t{\n"
                 + '\t\t.konamiID = "' + str(card_info[card]['id']) + '",\n'
                 + '\t\t.cardName = "' + card_info[card]['name'].replace('"', '') + '",\n')
    try:
        output.write("\t\t.atk = " + str(card_info[card]['atk']) + ",\n"
                    + "\t\t.defn = " + str(card_info[card]['def']) + ",\n"
                    + "\t\t.level = " + str(card_info[card]['level']) + ",\n"
                    + "\t\t.race = RACE_" + re.sub(r'\W+', '_', card_info[card]['race']).upper() + ",\n"
                    + "\t\t.attribute = ATTRIBUTE_" + card_info[card]['attribute'] + ",\n")
    except:
        output.write("\t\t.atk = 0,\n"
                    + "\t\t.defn = 0,\n"
                    + "\t\t.level = 0,\n"
                    + "\t\t.race = RACE_NONE,\n"
                    + "\t\t.attribute = ATTRIBUTE_NONE,\n")
    output.write("\t\t.type = TYPE_" + re.sub(r'\W+', '_', card_info[card]['type'].replace(" Monster", "").replace(" Card", "")).upper() + ",\n"
                    + '\t},\n')

# count = 0
# for card in card_info:
#     output.write('#define ' + re.sub(r'\W+', '_', card_info[card]['name']).upper() + ' ' + str(count) + '\n')
#     count += 1

output_ = open('output.txt', 'w', encoding='utf8')
count = 0
for pack in list(set_chronology_tcg):
    output_.write('#define PACK_TCG_' + re.sub(r'\W+', '_', set_chronology_tcg[pack][0].upper()) + ' ' + str(count) + '\n')
    count += 1