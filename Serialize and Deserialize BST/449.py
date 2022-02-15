import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root: TreeNode) -> str:
    if root == None:
        return "null"
    s = str(root.val)
    left = serialize(root.left)
    right = serialize(root.right)
    return s + "," + left + "," + right

def serialize_que(root: TreeNode) -> str:
    if root is None:
        return ""
    ans = ""
    que = []
    que.append(root)
    while(que):
        node = que.pop(0)
        if node is None:
            ans = ans + "n"
        else:
            ans = ans + str(node.val)
            
            que.append(node.left)
            que.append(node.right)
    
    return ans

def deserialize(data: str) -> TreeNode:
    if not data or len(data) == 0:
        return None

    dataque = []
    for i in data:
        if i is not "n":
            dataque.append(i)
        else:
            dataque.append(None)
    
    root = TreeNode(dataque.pop(0))
    que = []
    que.append(root)

    while(que):
        node = que.pop(0)
        left = dataque.pop(0)
        right = dataque.pop(0)

        if left:
            node.left = TreeNode(left)
            que.append(node.left)

        if right:
            node.right = TreeNode(right)
            que.append(node.right)

    return root
        

p = None
# p.left = TreeNode(1) 
# p.right = TreeNode(4)
# p.left.left = TreeNode(5)
# p.left.right = TreeNode(3)
# p.right.left = None
# p.right.right = TreeNode(6)

serialized = serialize_que(p)
print(serialized)

# deserialized = deserialize(serialized)

# reserialized = serialize_que(deserialized)

# print(reserialized)
