# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None:
        return None
    nodes = []
    while head is not None:
        nodes.append(head.val)
        head = head.next
    
    nodes = nodes[::-1]
    if k >= len(nodes):
        k = k % len(nodes)
    for i in range(k):
        t = nodes[0]
        nodes = nodes[1:]
        nodes.append(t)
        
    nodes = nodes[::-1]
    head = ListNode(nodes[0])
    headref = head
    
    for i in range(1, len(nodes)):
        head.next = ListNode(nodes[i])
        head = head.next
        
    return headref