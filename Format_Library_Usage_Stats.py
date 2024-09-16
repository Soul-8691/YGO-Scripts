from collections import Counter
import requests

# This code gets the most used decks of all recent events of a particular format
f = "yugi-kaiba"
site = "https://www.formatlibrary.com"

finalised_data = dict()

dt = requests.get(f"{site}/api/events/recent/{f}").json()["events"]
for event_info in dt:
    print(f"Going through {event_info['abbreviation']} event's decks")
    event = requests.get(f"{site}/api/events/{event_info['abbreviation']}?isAdmin=false&isSubscriber=false").json()
    decks = []
    finalised_data[event_info["abbreviation"]] = decks
    for deck_info in event["topDecks"]:
        deck = requests.get(f"{site}/api/decks/{deck_info['id']}?isAdmin=false&isSubscriber=false").json()
        decks.append({
            "main": [c["name"] for c in deck["main"]],
            "extra": [c["name"] for c in deck["extra"]],
            "side": [c["name"] for c in deck["side"]]
        })

output = open('output.txt', 'w', encoding='utf8')

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

output.write('Main deck:\n')
cards_main.sort()
card_counts = Counter(cards_main).most_common()
for key, value in card_counts:
    output.write(key + ': ' + str(value) + '\n')

output.write('\nSide deck:\n')
cards_side.sort()
card_counts = Counter(cards_side).most_common()
for key, value in card_counts:
    output.write(key + ': ' + str(value) + '\n')

output.write('\nExtra deck:\n')
cards_extra.sort()
card_counts = Counter(cards_extra).most_common()
for key, value in card_counts:
    output.write(key + ': ' + str(value) + '\n')

output.write('\nAll decks:\n')
cards_all.sort()
card_counts = Counter(cards_all).most_common()
for key, value in card_counts:
    output.write(key + ': ' + str(value) + '\n')

output.close()