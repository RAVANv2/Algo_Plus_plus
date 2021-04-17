class Solution:
    # Function to rotate a linked list.
    def rotate(self, head, k):
        l = 0
        ptr1 = head
        while ptr1:
            ptr1 = ptr1.next
            l += 1
        if l == k:
            return head

        ptr1 = head
        ptr2 = head
        while ptr2.next != None:
            ptr2 = ptr2.next

        while k:
            ptr2.next = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            k -= 1
        head = ptr2.next
        ptr2.next = None
        return head