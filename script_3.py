import json
from dateutil import parser
from datetime import *

f = open('YGOProDeck_Card_Info.json')
f2 = open('Set_Chronology.json')
data = json.load(f)
data2 = json.load(f2)
card_info = {}
for card_info_data in data['data']:
    card_info[card_info_data['name']] = card_info_data
yugikaiba = date(2002, 3, 29)

for card in data2:
    for set in data2[card]:
        try:
            date_ = parser.parse(data2[card][set]['set_chronology'][1]).date()
            if date_ <= yugikaiba:
                attribute = 'None'
                level = 0
                atk = 0
                defn = 0
                try:
                    attribute = card_info[card]['attribute']
                    level = card_info[card]['level']
                    atk = card_info[card]['atk']
                    defn = card_info[card]['def']
                    print(card + '\t' + card_info[card]['type'] + '\t' + attribute + '\t' + card_info[card]['race'] + '\t' + str(level) + '\t' + str(atk) + '\t' + str(defn) + '\t' + str(card_info[card]['id']) + '\t' + set + '\t' + data2[card][set]['set_chronology'][1])
                    break
                except:
                    print(card + '\t' + card_info[card]['type'] + '\t' + attribute + '\t' + card_info[card]['race'] + '\t' + str(level) + '\t' + str(atk) + '\t' + str(defn) + '\t' + str(card_info[card]['id']) + '\t' + set + '\t' + data2[card][set]['set_chronology'][1])
                    break
        except:
            pass

f.close()
f2.close()