class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def contains(root: Node, search: int) -> bool:
  if root is None:
    return False
  if root.val == search:
    return True
  if search < root.val:
    return contains(root.left, search)
  elif search > root.val:
    return contains(root.right, search)


p = Node(2)
p.left = Node(1) 
p.right = Node(4)
p.left.left = Node(3)
p.left.right = Node(5)

print(contains(p, 1))
