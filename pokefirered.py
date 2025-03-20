import json
from set_chronology import set_chronology_ocg, set_chronology_tcg

f = open('YGOProDeck_Card_Info.json')
data = json.load(f)
card_info = {}
for card_info_data in data['data']:
    card_info[card_info_data['name']] = card_info_data