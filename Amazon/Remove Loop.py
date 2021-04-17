def removeLoop(head):
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None
    return