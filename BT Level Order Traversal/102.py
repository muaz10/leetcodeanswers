class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printLevelOrder(root):
  def height(head):
    if head is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(head.left)
        rheight = height(head.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
          
  currentLevel = []
  trav = []
  def printCurrentLevel(head, level):
      if head is None:
          return
      if level == 1:
          # print(str(head.val) + " ")
          currentLevel.append(head.val)
      elif level > 1:
          printCurrentLevel(head.left, level-1)
          printCurrentLevel(head.right, level-1)

  h = height(root)
  for i in range(1, h+1):
      currentLevel = []
      printCurrentLevel(root, i)
      trav.append(currentLevel)
  return trav


p = Node(2)
p.left = Node(1) 
p.right = Node(4)
p.left.left = Node(5)
p.left.right = Node(3)

print(printLevelOrder(p))
# printLevelOrder(p)
