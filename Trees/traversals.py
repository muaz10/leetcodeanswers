class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A function to do inorder tree traversal
def printInorder(root):    
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do preorder tree traversal
def printPreorder(root):    
    if root:    
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):    
    if root:    
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val)

def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
 
        # Print front of queue and
        # remove it from queue
        print(queue[0].val)
        node = queue.pop(0)
 
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

p = Node(2)
p.left = Node(1) 
p.right = Node(4)
p.left.left = Node(5)
p.left.right = Node(3)

printLevelOrder(p)
