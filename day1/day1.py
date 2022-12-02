import time

start = time.time()

with open('./day1.txt') as f:
	calories = f.read()

	split = calories.split('\n')
	final = []
	summation = 0
	for x in split:
		if x == '':
			final.append(summation)
			summation = 0
		else:
			summation += int(x)

	final.append(summation)

	final.sort()
	print('Top 1: {}'.format(final[-1]))
	print('Top 3: {}'.format(final[-1] + final[-2] + final[-3]))

end = time.time()

print(end - start)
