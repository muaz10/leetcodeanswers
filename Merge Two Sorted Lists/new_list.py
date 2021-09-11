def merge_two_sorted_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  if l1 == None and l2 == None:
    return None
  elif l1 == None:
    return l2
  elif l2 == None:
    return l1
  else:
    if l1.val <= l2.val:
      l3 = ListNode(l1.val)
      l1 = l1.next
    else:
      l3 = ListNode(l2.val)
      l2 = l2.next
    res = l3
    
    while l1 != None and l2 != None:
      if l1.val <= l2.val:
        l3.next = ListNode(l1.val)
        l3 = l3.next
        l1 = l1.next
      else:
        l3.next = ListNode(l2.val)
        l3 = l3.next
        l2 = l2.next
    
    while l1 != None:
      l3.next = ListNode(l1.val)
      l3 = l3.next
      l1 = l1.next
        
    while l2 != None:
      l3.next = ListNode(l2.val)
      l3 = l3.next
      l2 = l2.next

    return res