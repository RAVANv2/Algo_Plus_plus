def findMid(head):
    l = 0
    ptr = head
    while ptr:
        l += 1
        ptr = ptr.next
    idx = l//2
    i = 1
    while i<=idx:
        i += 1 
        head = head.next
    return head.data