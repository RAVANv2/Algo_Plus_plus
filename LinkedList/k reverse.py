# Given a head to Linked List L, write a function to reverse the list taking k elements at a time. Assume k is a factor of the size of List.
# You need not have to create a new list. Just reverse the old one using head.

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def kreverse(self, head,k):
        curr = head
        next = None
        prev = None
        count = 0

        while count<k and curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next:
            head.next = self.kreverse(next,k)

        return prev

    def printList(self,head):
        while head:
            print(head.data,end=' ')
            head = head.next

n,k = list(map(int,input().strip().split()))

array = list(map(int,input().strip().split()))

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    new = node(ele)
    temp.next = new
    temp = temp.next

ans = ll.kreverse(ll.head,k)
ll.printList(ans)
