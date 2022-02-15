import collections

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def printLevelOrder(root, target):
    # Base Case
    if root is None:
        return
 
    # Create an empty queue
    # for level order traversal
    queue = collections.deque()
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(queue):
 
        # Print front of queue and
        # remove it from queue
        node = queue.popleft()
        if node.val == target:
          return
 
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:

