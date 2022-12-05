import copy

def printTopOfStacks(stacks):
	topOfStacks = []
	for stack in stacks.values():
		if len(stack) > 0:
			topOfStacks.append(stack[-1])
	return ''.join(topOfStacks)

with open('./day5.txt') as f:
	lines = f.read().split('\n')

	# setup
	split = lines.index('')
	diagram = lines[:split]
	stackNumbers = diagram.pop().split()
	stackContent = diagram[::-1]
	instructions = lines[split + 1:]
	stacks = {}
	for x in stackNumbers:
		stacks[x] = []

	# set up of indeces of where to read in diagram line
	indeces = []
	position = 1
	while position <= len(diagram[0]):
		indeces.append(position)
		position += 4

	# create stacks
	for contentLine in stackContent:
		for i in range(len(indeces)):
			if contentLine[indeces[i]] != ' ':
				stacks[str(i + 1)].append(contentLine[indeces[i]])
	stacks1 = stacks
	stacks2 = copy.deepcopy(stacks)

	# execute instructions v1
	for instruction in instructions:
		words = instruction.split(' ')
		numberToMove = int(words[1])
		fromStack = words[3]
		toStack = words[5]

		for i in range(numberToMove):
			stacks1[toStack].append(stacks1[fromStack].pop())

	# execute isntructions v2
	for instruction in instructions:
		words = instruction.split(' ')
		numberToMove = int(words[1])
		fromStack = words[3]
		toStack = words[5]

		start = len(stacks2[fromStack]) - numberToMove
		stacks2[toStack] += stacks2[fromStack][start:]
		del stacks2[fromStack][start:]

	# get top of stacks
	print(printTopOfStacks(stacks1))
	print(printTopOfStacks(stacks2))
