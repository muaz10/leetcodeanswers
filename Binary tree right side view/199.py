class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binaryTreeRightSideView(root):
    if root is None:
        return

    queue = []
    left = []
    right = [] 
    queue.append(root)
 
    while(len(queue) > 0):
        lastIndex = len(queue)-1
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == 0:
                left.append(node.val)
            if i == lastIndex:
                right.append(node.val)

    left = left[::-1]
    for i in range(1, len(right)):
        left.append(right[i])

    print(left)

p = Node(1)
p.left = Node(2) 
p.right = Node(3)
p.left.right = Node(5)
p.left.left = Node(6)
p.right.right = Node(4)
p.right.left = Node(7)

binaryTreeRightSideView(p)