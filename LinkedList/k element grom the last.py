# Given a linked list with n nodes. Find the kth element from last without computing the length of the linked list.

# Solution:
    # Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head. First, move the reference pointer to n nodes from head. Now move both pointers one by one until the reference pointer reaches the end. Now the main pointer will point to nth node from the end. Return the main pointer.

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        while head:
            print(head.data, end=' ')
            head = head.next

    def kFromLast(self, head, k):
        p1 = p2 = head
        k -= 1
        while k:
            p1 = p1.next
            k -= 1

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        print(p2.data)

array = list(map(int, input().strip().split()))
k = int(input())

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    if ele == -1:
        break
    new = node(ele)
    temp.next = new
    temp = temp.next

ll.kFromLast(ll.head,k)