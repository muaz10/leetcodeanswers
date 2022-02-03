from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def printPreorder(root):    
  if root:    
    # First print the data of node
    print(root.val),

    # Then recur on left child
    printPreorder(root.left)

    # Finally recur on right child
    printPreorder(root.right)

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
  if p.val == None and q.val == None:
    return True
  if p.val == None or q.val == None:
    return False

  printPreorder(p)

  return True

p = TreeNode(1)
p.left = TreeNode(2) 
p.right = TreeNode(3)
p.right.left = TreeNode(4)
p.right.right = TreeNode(5)

isSameTree(p, p)
