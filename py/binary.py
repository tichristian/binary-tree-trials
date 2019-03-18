class Node:
    """
    Binary tree class
    """
    def __init__(self, *argv):

        self.data = None
        self.left = None
        self.right = None
        self.side = '-'
        self.level = 1

        for arg in argv:
            self.insert(arg)
        
    def insert(self, data):
        # inserts the value of the tree left < node < right

        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.left.level += self.level
                self.left.side = 'l'
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                self.right.level += self.level
                self.right.side = 'r'
            else:
                self.right.insert(data)
        
    def printtree(self):
        # print all data of the tree
        if self.left:
            self.left.printtree()

        print('{0}({1}) {2}'.format(self.level, self.side, self.data)),

        if self.right:
            self.right.printtree()

    def closestvalue(self, data):
        # gets the closest value
        closest = {'level': self.level, 'value': self.data}
        nextclosest = {'value': 0}
                
        if data < self.data and self.left is not None:
            nextclosest = self.left.closestvalue(data)
        elif data > self.data and self.right is not None:
            nextclosest = self.right.closestvalue(data)
        
        if abs(nextclosest['value'] - data) < abs(closest['value'] - data):
            closest = nextclosest
            
        return closest

    def deletelevel(self, level):
        # delete a level of the tree

        if abs(self.level - level) == 1:
            self.left = None
            self.right = None
        
        if self.right:
            self.right.deletelevel(level)
        if self.left:
            self.left.deletelevel(level)
        
    def __str__(self):
        return '{0}'.format(self.data)

    
if __name__ == '__main__':
    # execute if ran as script
    root = Node(12)
    tree = Node(12, 3, 4, 6, 16, 20, 14, 15)

    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(20)
    root.insert(13)
    root.insert(17)
    
    print('print(root): {0}'.format(root))
    print('---')
    print('root.insert(6)')
    print('root.insert(14)')
    print('root.insert(3)')
    print('root.insert(7)')
    print('root.insert(20)')
    print('root.insert(13)')
    print('root.insert(17)')
    root.printtree()
    print('---')
    print('tree = Node(12, 3, 4, 6, 16, 20, 14, 15)')
    tree.printtree()
    print('---')
    print('tree.closestvalue(14):')
    print(tree.closestvalue(14))
    print('tree.closestvalue(19):')
    print(tree.closestvalue(19))
    print('tree.closestvalue(5):')
    print(tree.closestvalue(5))
    print('tree.closestvalue(6):')
    print(tree.closestvalue(6))

    print('---')
    tree.deletelevel(4)
    print('tree.deletelevel(4)')
    tree.printtree()
