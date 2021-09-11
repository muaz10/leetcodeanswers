def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  if l1 == None and l2 == None:
    return None
  elif l1 == None:
    return l2
  elif l2 == None:
    return l1
  else:
    if l1.val > l2.val:
      temp = l1
      l1 = l2
      l2 = temp
    res = l1
    while l1.next != None:
      if l1.next.val > l2.val:
        temp = l1.next
        l1.next = l2
        l1 = l1.next
        l2 = temp
      else:
        l1 = l1.next
    l1.next = l2
    return res
