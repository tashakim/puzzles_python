import itertools, random

cards = []
for i in range(1,10):
	cards.append(i)
cards.append('Jack')
cards.append('Queen')
cards.append('King')
cards.append('Ace')

suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
deck = list(itertools.product(cards, suit))

random.shuffle(deck)

print("You drew the cards: ")
for i in range(5):
	print(deck[i][0], "of", deck[i][1])


