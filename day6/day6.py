def findMarker(markerLen):
	countDict = {}

	def udpateCountAndIsMarker(char, removeChar=None):
		if char in countDict:
			countDict[char] += 1
		else:
			countDict[char] = 1

		if removeChar:
			if countDict[removeChar] == 1:
				del countDict[removeChar]
			else:
				countDict[removeChar] -= 1

		return len(countDict) == markerLen

	# udpate countDict with the first markerLen chars
	for i in range(markerLen):
		if udpateCountAndIsMarker(stream[i]):
			return markerLen

	position = markerLen

	# loop through the rest of the stream
	while position < len(stream):
		if udpateCountAndIsMarker(stream[position], stream[position - markerLen]):
			return position + 1
		position += 1

with open('./day6.txt') as f:
	stream = f.read()
	markerLen1 = 4
	markerLen2 = 14

	print(findMarker(markerLen1))
	print(findMarker(markerLen2))

