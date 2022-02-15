def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node, path, target):
        if node == None:
            return None
        if node.val == target.val:
            path.append(node)
            return path
        path.append(node)
        result = dfs(node.left, path.copy(), target)
        if (result != None):
            return result
        result = dfs(node.right, path.copy(), target)
        if (result != None):
            return result
        
    emp1Path = set(dfs(root, [], p))
    emp2Path = dfs(root, [], q)
    
    for i in range(len(emp2Path)-1, -1, -1):
        if emp2Path[i] in emp1Path:
            return emp2Path[i]