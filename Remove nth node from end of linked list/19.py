from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  if head is None:
    return head
  arr = []
  while head:
    arr.insert(0, head.val)
    head = head.next
  
  arr.pop(n-1)
  ans = ListNode(arr[0])
  tail = ans
  for i in range(len(arr)-1, -1, -1):    
    tail.next = ListNode(arr[i])
    tail = tail.next



a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
removeNthFromEnd(a, 4)
