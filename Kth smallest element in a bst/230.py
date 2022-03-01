# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif(stack):
                current = stack.pop()
                self.count += 1
                if self.count == k:
                    return current.val
                current = current.right

            else:
                break

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        ans = 0
        c=0
        def inOrderTrav(root):
            nonlocal ans
            nonlocal c
            if not root:
                return
            if root.left:
                inOrderTrav(root.left)
            c+=1
            if (c==k):
                ans = root.val
                return
            if root.right:
                inOrderTrav(root.right)
        inOrderTrav(root)
        return ans