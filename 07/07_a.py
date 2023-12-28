import os
from functools import cmp_to_key

path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


def get_hand_type(hand):
    m = {card: hand.count(card) for card in set(hand)}

    key_len = len(m.keys())
    if key_len == 1:
        return 6
    if key_len == 2:
        if 4 in m.values():
            return 5
        else:
            return 4
    if key_len == 3:
        if 3 in m.values():
            return 3
        else:
            return 2
    if key_len == 4:
        return 1
    return 0


def compare_pairs(pair1, pair2):
    hand1, _ = pair1
    hand2, _ = pair2

    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)

    if hand1_type < hand2_type:
        return 1
    if hand1_type > hand2_type:
        return -1

    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            return 1 if card_ranking.index(hand1[i]) > card_ranking.index(hand2[i]) else -1

card_ranking = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

pairs = [(line.split()[0], int(line.split()[1])) for line in lines]
sorted_pairs = sorted(pairs, key=cmp_to_key(compare_pairs), reverse=False)

winnings = 0
for i, (hand, bid) in enumerate(sorted_pairs):
    rank = len(sorted_pairs) - i
    winnings += bid * rank

print(winnings)