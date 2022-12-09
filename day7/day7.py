from collections import deque

class TreeNode:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.size = 0
        self.children = {}

    def __str__(self):
        return '[name: {0}, size: {1}, parent: {2}, children: {3}]'.format(self.name, self.size, self.parent, self.children)

def calculateSizes(root):
	queue = deque([root])
	while len(queue) > 0:
		currentNode = queue.popleft()
		for childValue in currentNode.children.values():
			if type(childValue) is int:
				parentNode = currentNode
				while parentNode != None:
					parentNode.size += childValue
					parentNode = parentNode.parent
			else:
				queue.append(childValue)

	return root

def calculateSum(root, limit):
	queue = deque([root])
	summation = 0
	while len(queue) > 0:
		currentNode = queue.popleft()
		if currentNode.size <= limit:
			summation += currentNode.size
		for childValue in currentNode.children.values():
			if type(childValue) is not int:
				queue.append(childValue)

	return summation

def smallestSizeToDelete(root, limit):
	queue = deque([root])
	smallestSize = float('inf')
	while len(queue) > 0:
		currentNode = queue.popleft()
		if currentNode.size >= limit and currentNode.size < smallestSize:
			smallestSize = currentNode.size
		for childValue in currentNode.children.values():
			if type(childValue) is not int:
				queue.append(childValue)

	return smallestSize

with open('./day7.txt') as f:
    lines = f.read().split('\n')

    limit = 100000
    totalMemory = 70000000
    requiredMemory = 30000000
    lineNum = 1
    root = TreeNode('/', None)
    currentNode = root

    # build tree
    while lineNum < len(lines):
        splitLine = lines[lineNum].split(' ')
        if splitLine[1] == 'cd':
            if splitLine[2] == '..':
                currentNode = currentNode.parent
            else:
                currentNode = currentNode.children[splitLine[2]]

        elif splitLine[1] == 'ls':
            while True:
                lineNum += 1
                if lineNum >= len(lines):
                    break
                innerSplitLine = lines[lineNum].split(' ')

                if innerSplitLine[0] == '$':
                    lineNum -= 1
                    break
                elif innerSplitLine[0] == 'dir':
                    newNode = TreeNode(innerSplitLine[1], currentNode)
                    currentNode.children[innerSplitLine[1]] = newNode
                else:
                    currentNode.children[innerSplitLine[1]] = int(innerSplitLine[0])
        lineNum += 1

    calculateSizes(root)

    print(calculateSum(root, limit))

    currentAvailableMemory = totalMemory - root.size
    memoryToRemove = requiredMemory - currentAvailableMemory
    print(smallestSizeToDelete(root, memoryToRemove))
