import json
from dateutil import parser
from datetime import *
import traceback
import logging

f = open('YGOProDeck_Card_Info.json')
f2 = open('Set_Chronology.json')
data = json.load(f)
data2 = json.load(f2)
card_info = {}
for card_info_data in data['data']:
    card_info[card_info_data['name']] = card_info_data
yugikaiba = date(2002, 3, 29)
critter = date(2002, 6, 26)
treasure = date(2002, 9, 16)
eds = date(2002, 10, 15)
imperial = date(2002, 10, 20)
android = date(2003, 3, 1)
warrior = date(2004, 12, 1)
reaper = date(2006, 2, 18)
gladiator = date(2008, 8, 1)

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

output = open('output.txt', 'w', encoding='utf8')
monster_types = ['Normal', 'Effect', 'Ritual', 'Fusion']
counter = 821

for card in card_info:
    # count = 0
    # for set in data2[card]:
    #     try:
    #         date_ = parser.parse(data2[card][set]['set_chronology_tcg'][1]).date()
    #         if date_ <= critter:
    #             attribute = 'None'
    #             level = 0
    #             atk = 0
    #             defn = 0
    #             try:
    #                 attribute = card_info[card]['attribute']
    #                 level = card_info[card]['level']
    #                 atk = card_info[card]['atk']
    #                 defn = card_info[card]['def']
    #                 if count == 0:
    #                     output.write(card + '\t' + card_info[card]['type'] + '\t' + attribute + '\t' + card_info[card]['race'] + '\t' + str(level) + '\t' + str(atk) + '\t' + str(defn) + '\tY\n')
    #             except:
    #                 if count == 0:
    #                     output.write(card + '\t' + card_info[card]['type'] + '\t' + attribute + '\t' + card_info[card]['race'] + '\t' + str(level) + '\t' + str(atk) + '\t' + str(defn) + '\tY\n')
    #             count = count + 1
    #     except:
    #         pass
    attribute = 'None'
    level = 0
    atk = 0
    defn = 0
    desc = card_info[card]['desc']
    passw = str(card_info[card]['id']).zfill(8)
    monster_type = card_info[card]['type'].replace(' Monster', '').replace(' Card', '')
    race = card_info[card]['race']
    # if monster_type == 'Ritual Effect':
    #     monster_type = 'Ritual'
    # if monster_type == 'Spell':
    #     race = 'Spell'
    #     monster_type = 'Normal'
    # if monster_type == 'Trap':
    #     race = 'Trap'
    #     monster_type = 'Normal'
    # if monster_type not in monster_types:
    #     monster_type = 'Effect'
    # if monster_type == 'Normal':
    #     monster_type = 'Monster'
    try:
        attribute = card_info[card]['attribute']
        level = card_info[card]['level']
        atk = card_info[card]['atk']
        defn = card_info[card]['def']
    except:
        pass
    output.write(card + '\t' + card_info[card]['type'] + '\t' + attribute + '\t' + card_info[card]['race'] + '\t' + str(level) + '\t' + str(atk) + '\t' + str(defn) + '\t' + desc.replace('\r\n', ' ').replace('\n', ' ') + '\n')
# 	},
# ''')
        # counter += 1

f.close()
f2.close()