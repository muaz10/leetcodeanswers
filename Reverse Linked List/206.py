class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    linkedlist = []
    while head:
        linkedlist.append(head.val)
        head = head.next

    reverse = ListNode(linkedlist[-1])
    ans = reverse

    for i in range(len(linkedlist)-2, -1, -1):
        reverse.next = ListNode(linkedlist[i])
        reverse = reverse.next

    return ans
