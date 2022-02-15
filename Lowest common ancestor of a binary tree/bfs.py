def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def bfs(target, root):
        que = collections.deque([(root,[])])
        while (que):
            (n, path) = que.popleft()
            if n == None:
                continue
            path.append(n.val)
            if n.val == target.val:
                return path
            que.append((n.left, path.copy()))
            que.append((n.right, path.copy()))
        
    emp1Path = set(dfs(root, [], p))
    emp2Path = dfs(root, [], q)
    
    for i in range(len(emp2Path)-1, -1, -1):
        if emp2Path[i] in emp1Path:
            return emp2Path[i]