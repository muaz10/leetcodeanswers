Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set()
    root = head
    ans = head
    while head:
        if head.val in nums:
            root.next = head.next
            head = head.next
        else:
            nums.add(head.val)
            root = head
            head = head.next
            
    
    return ans
