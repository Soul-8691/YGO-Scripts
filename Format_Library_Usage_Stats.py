from collections import Counter
import requests
import json

# This code gets the most used decks of all recent events of a particular format
# formats_json = open('formats.json', 'r', encoding='utf8')
# formats_json = json.load(formats_json)
# formats = list()
# for format in formats_json:
#     formats.append(format['name'].lower())
site = "https://www.formatlibrary.com"

# output = open('output.txt', 'w', encoding='utf8')
output_sheets = open('output.tsv', 'w', encoding='utf8')

formats = ['yugi-kaiba', 'critter','treasure', 'imperial', 'android', 'joey-pegasus', 'fiber', 'yata', 'scientist', 'vampire', 'chaos', 'warrior', 'goat', 'cyber', 'reaper', 'chaos return', 'stein', 'chimeratech', 'airblade', 'demise', 'trooper', 'zombie', 'perfect circle', 'phantom', 'dad return', 'gladiator', 'teledad', 'cat', 'lightsworn', 'edison', 'frog', 'x-saber', 'starstrike', 'six samurai', 'trishula', 'librarian', 'tengu plant', 'underworld', 'shockwave', 'long beach', 'dino rabbit', 'wind-up', 'miami', 'meadowlands', 'baby ruler', 'ravine ruler', 'fire-water', 'vegas', 'hat', 'shaddoll', 'burning abyss', 'charleston', 'nekroz', 'clown', 'pepe', 'dracopal', 'monarch', 'abc', 'grass zoo', 'draco zoo', 'link zoo', 'spyral', 'magician', 'secaucus', 'danger', 'striker', 'thunder dragon', 'lunalight', 'toss', 'rokket', 'adamancipator', 'infernoble', 'virtual world', 'dragon link', 'tri zoo', 'bird-up', 'phoenix', 'despia', 'elements', 'minneapolis', 'tearlaments', 'rescue-ace', 'snake-eye', 'traditional', 'current']

used_cards = dict()
cumulative = dict()
total = dict()

for f in formats:
    finalised_data = dict()
    dt = requests.get(f"{site}/api/events/recent/{f}").json()["events"]
    for event_info in dt:
        print(f"Going through {f + ' ' + event_info['abbreviation']} event's decks")
        event = requests.get(f"{site}/api/events/{event_info['abbreviation']}?isAdmin=false&isSubscriber=false").json()
        decks = []
        finalised_data[event_info["abbreviation"]] = decks
        for deck_info in event["topDecks"]:
            deck = requests.get(f"{site}/api/decks/{deck_info['id']}?isAdmin=false&isSubscriber=false").json()
            try:
                decks.append({
                    "main": [c["name"] for c in deck["main"]],
                    "extra": [c["name"] for c in deck["extra"]],
                    "side": [c["name"] for c in deck["side"]]
                })
            except Exception as e:
                pass

    cards_all = []
    cards_main = []
    cards_side = []
    cards_extra = []

    for tour in finalised_data:
        for deck in finalised_data[tour]:
            for card in deck['main']:
                cards_main.append(card)
                cards_all.append(card)
            for card in deck['side']:
                cards_side.append(card)
                cards_all.append(card)
            for card in deck['extra']:
                cards_extra.append(card)
                cards_all.append(card)

    cards_all.sort()
    card_counts = Counter(cards_all).most_common()
    for key, value in card_counts:
        if key not in used_cards:
            used_cards[key] = dict()
            cumulative[key] = 0
            total[key] = 0
        cumulative[key] += value
        total[key] += value
        used_cards[key][f] = {'amount': value, 'cumulative': cumulative[key], 'total': 0}

for key in used_cards:
    for f in used_cards[key]:
        used_cards[key][f]['total'] = total[key]

output_sheets.write('Card\tFormat\tUsage\tCumulative\tTotal\tFormat Index\n')

for card in used_cards:
    for format in used_cards[card]:
        output_sheets.write(card + '\t' + format + '\t' + str(used_cards[card][format]['amount']) + '\t' + str(used_cards[card][format]['cumulative']) + '\t' + str(used_cards[card][format]['total']) + '\t' + str(formats.index(format)) + '\n')

# output.write('Main deck:\n')
# cards_main.sort()
# card_counts = Counter(cards_main).most_common()
# for key, value in card_counts:
#     output.write(key + ': ' + str(value) + '\n')

# output.write('\nSide deck:\n')
# cards_side.sort()
# card_counts = Counter(cards_side).most_common()
# for key, value in card_counts:
#     output.write(key + ': ' + str(value) + '\n')

# output.write('\nExtra deck:\n')
# cards_extra.sort()
# card_counts = Counter(cards_extra).most_common()
# for key, value in card_counts:
#     output.write(key + ': ' + str(value) + '\n')

# output.write('\nAll decks:\n')
# cards_all.sort()
# card_counts = Counter(cards_all).most_common()
# for key, value in card_counts:
#     output.write(key + ': ' + str(value) + '\n')

# output.close()
output_sheets.close()