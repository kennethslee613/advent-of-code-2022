alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = {}
for i in range(len(alphabet)):
	alphaDict[alphabet[i]] = i + 1

def getValueOfIntersectionChar(A):
	intersection = set(A[0])
	for i in range(1, len(A)):
		intersection = intersection.intersection(set(A[i]))

	return alphaDict[intersection.pop()]

with open('./day3.txt') as f:
	rucksacks = f.read().split('\n')

	# Part 1
	summation = 0

	for x in rucksacks:
		mid = len(x) // 2
		a = x[:mid]
		b = x[mid:]

		summation += getValueOfIntersectionChar([a, b])

	print(summation)

	# Part 2
	summation2 = 0

	for i in range(0, len(rucksacks), 3):
		a = rucksacks[i]
		b = rucksacks[i + 1]
		c = rucksacks[i + 2]

		summation2 += getValueOfIntersectionChar([a, b, c])

	print(summation2)

