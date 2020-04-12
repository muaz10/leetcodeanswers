def middleotLL(head):
    length = 1
    half = head
    while head != None:
        if length % 2 == 0:
            half = half.next
        length += 1
        head = head.next

    return half
