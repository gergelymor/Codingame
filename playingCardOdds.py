import sys
import math

r, s = [int(i) for i in input().split()]
removed = []
sought = []

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["C", "D", "H", "S"]

allCardsMatrix = [f"{x}{y}" for x in ranks for y in suits]
allCards = set()

for card in allCardsMatrix:
    allCards.add(card)
removedCards = set()
remainingCards = set()
soughtCards = set()

for i in range(r):
    re = input()
    removed.append(re)
for i in range(s):
    so = input()
    sought.append(so)

for i in removed:
    tempRanks = []
    tempSuits = []
    for cardRankOrSuit in i:
        if cardRankOrSuit in ranks:
            tempRanks.append(str(cardRankOrSuit))
        elif cardRankOrSuit in suits:
            tempSuits.append(str(cardRankOrSuit))
    if not tempRanks:
        tempRanks = ranks
    if not tempSuits:
        tempSuits = suits
    removedInThisIteration = [f"{x}{y}" for x in tempRanks for y in tempSuits]
    for card in removedInThisIteration:
        removedCards.add(card)

for i in sought:
    tempRanks = []
    tempSuits = []
    for cardRankOrSuit in i:
        if cardRankOrSuit in ranks:
            tempRanks.append(str(cardRankOrSuit))
        elif cardRankOrSuit in suits:
            tempSuits.append(str(cardRankOrSuit))
    if not tempRanks:
        tempRanks = ranks
    if not tempSuits:
        tempSuits = suits
    soughtInThisIteration = [f"{x}{y}" for x in tempRanks for y in tempSuits]
    for card in soughtInThisIteration:
        soughtCards.add(card)

remainingCards = allCards - removedCards

validSoughtCards = soughtCards & remainingCards

if len(remainingCards) == 0:
    print("0%")
else:
    probability = (len(validSoughtCards) / len(remainingCards)) * 100
    print(f"{round(probability)}%")
