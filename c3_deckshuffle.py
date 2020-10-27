from random import choice

suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

pack = []
suitCount = []

deckLength = 52
count = 0

while count != deckLength:
  check = True

  cardSuit = choice(suits)
  cardRank = choice(ranks)

  newCard = str(cardRank + ' ' + cardSuit)

  for card in pack:
    if card == newCard:
      check = False
  
  if check == True:
    count += 1
    suitCount.append(cardSuit)
    pack.append(newCard)

print(pack)
print(suitCount)