import json
from set_chronology import set_chronology_tcg

f = open('YGOProDeck_Card_Info.json')
data = json.load(f)
card_info = {}
for card_info_data in data['data']:
    card_info[card_info_data['name']] = card_info_data

for set in set_chronology_tcg:
    if len(set_chronology_tcg[set]) == 2:
        print(set, list(set_chronology_tcg).index(set))