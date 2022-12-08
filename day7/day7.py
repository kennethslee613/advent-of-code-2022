class TreeNode:
    def __init__(self, name, parent, size=0, children={}):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = children

    def __str__(self):
        return '[name: {0}, size: {1}, parent: {2}, children: {3}]'.format(self.name, self.size, self.parent, self.children)

with open('./day7.txt') as f:
    lines = f.read().split('\n')

    limit = 100000
    summation = 0
    lineNum = 1
    root = TreeNode('/', None)
    head = root

    # calculate size of directories
    while lineNum < len(lines):
        print('one', head)
        splitLine = lines[lineNum].split(' ')
        if splitLine[1] == 'cd':
            print('cd', head)
            if splitLine[2] == '..':
                head = head.parent
            else:
                head = head.children[splitLine[2]]

        elif splitLine[1] == 'ls':
            print('ls')
            while True:
                lineNum += 1
                if lineNum >= len(lines):
                    break
                innerSplitLine = lines[lineNum].split(' ')
                print(innerSplitLine)

                if innerSplitLine[0] == '$':
                    lineNum -= 1
                    break
                elif innerSplitLine[0] == 'dir':
                    newNode = TreeNode(innerSplitLine[1], head)
                    print('newNode', newNode)
                    head.children[innerSplitLine[1]] = newNode
                else:
                    head.children[innerSplitLine[1]] = int(innerSplitLine[0])
        lineNum += 1

    print(head)
    print(root)
