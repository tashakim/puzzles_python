import itertools, random

deck = list(itertools.product(range(1,10), ['Spade', 'Heart', 'Diamond', 'Club']))

random.shuffle(deck)

print("You drew the cards: ")
for i in range(5):
	print(deck[i][0], "of", deck[i][1])


