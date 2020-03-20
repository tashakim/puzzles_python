perfectSquares  = []

for i in range(10): # range(10) is i<10.
	perfectSquares.append(i*i)

print(perfectSquares)

perfectSquares2 = []

for i in range(1, 11): # range(11) gives i<=10.
	perfectSquares2.append(i**2)

# print squares from 1^2 to 10^2.
print(perfectSquares2)