with open('./day4.txt') as f:
	pairs = f.read().split('\n')

	count = 0
	count2 = 0

	for pair in pairs:
		[elfOne, elfTwo] = pair.split(',')
		[elfOneFirst, elfOneSecond] = elfOne.split('-')
		[elfTwoFirst, elfTwoSecond] = elfTwo.split('-')

		if int(elfOneFirst) <= int(elfTwoFirst) and int(elfOneSecond) >= int(elfTwoSecond):
			count += 1
		elif int(elfOneFirst) >= int(elfTwoFirst) and int(elfOneSecond) <= int(elfTwoSecond):
			count += 1

		if int(elfOneSecond) >= int(elfTwoFirst) and int(elfOneFirst) <= int(elfTwoSecond):
			count2 += 1

	print(count)
	print(count2)
