def iterativePreorder(root):
     
    # Base Case
    if root is None:
        return
 
    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)
 
    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    def check(p, q):
        # if both are None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return True
    
    while(len(nodeStack) > 0):         
        # Pop the top item from stack and print it
        node = nodeStack.pop()
        if node is not None:
            if node.left is not None and node.left.val >= node.val:
                return False                    
            if node.right is not None and node.right.val <= node.val:
                return False
         
        # Push right and left children of the popped node
        # to stack
        if node is not None:
            nodeStack.append(node.left)
            nodeStack.append(node.right)
    
    return True

p = Node(2)
p.left = Node(1) 
p.right = Node(4)
p.right.left = Node(5)
p.right.right = Node(3)

print(iterativePreorder(p))


def iterativeInorder(root):
    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack
     
    while True:
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
         
            current = current.left
 
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.val, end=" ") # Python 3 printing
         
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
 
        else:
            break
      
def postOrderIterative(root):
    def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None
         
    # Check for empty tree
    if root is None:
        return

    ans = []
    stack = []
     
    while(True):         
        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
 
            # Set root as root's left child
            root = root.left
         
        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and peek(stack) == root.right):
            stack.pop() # Remove right child from stack
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the
                            # right childis processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.val)
            root = None
 
        if (len(stack) <= 0):
                break

    print(ans)