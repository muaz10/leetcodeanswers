class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(head: Node) -> Node:
        headref = head
        nodemap = {}
        
        if head is None:
            return None
        
        while head:
            nodemap[head] = Node(head.val)
            head = head.next
            
        head = headref
        
        while head:
            copy = nodemap[head]
            if head.next:
                copy.next = nodemap[head.next]
            else:
                copy.next = None
            if head.random:
                copy.random = nodemap[head.random]
            else:
                copy.random = None
            head = head.next
            
        return nodemap[headref]