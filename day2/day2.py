with open('./day2.txt') as f:
	strategy = f.read()

	split = strategy.split('\n')

	firstDictionary = {
		'A X': 3+1,
		'B X': 0+1,
		'C X': 6+1,
		'A Y': 6+2,
		'B Y': 3+2,
		'C Y': 0+2,
		'A Z': 0+3,
		'B Z': 6+3,
		'C Z': 3+3
	}
	secondDictionary = {
		'A X': 0+3,
		'B X': 0+1,
		'C X': 0+2,
		'A Y': 3+1,
		'B Y': 3+2,
		'C Y': 3+3,
		'A Z': 6+2,
		'B Z': 6+3,
		'C Z': 6+1
	}

	totalScore = 0
	secondTotalScore = 0

	for x in split:
		totalScore += firstDictionary[x]
		secondTotalScore += secondDictionary[x]

	print('first: {}'.format(totalScore))
	print('second: {}'.format(secondTotalScore))

