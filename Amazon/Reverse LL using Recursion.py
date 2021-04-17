def reverseList(head):
    if head is None:
        return head

    if head.next is None:
        return head

    node1 = reverseList(head.next)

    head.next.next = head
    head.next = None

    return node1