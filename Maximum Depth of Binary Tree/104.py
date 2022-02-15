class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
     
  def height(base: TreeNode) -> int:
    if base is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(base.left)
        rheight = height(base.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1 

  return height(root)