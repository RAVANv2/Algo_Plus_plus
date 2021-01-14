
# Given a linked list of length N and an integer K , append the last K elements of a linked list to the front. Note that K can be greater than N.

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self, head):
        while head:
            print(head.data, end=' ')
            head = head.next

    def kAppend(self, k, n, head):

        if k > n:
            k = k - n

        if k == n:
            return head

        front = n - k - 1
        temp = head
        while front:
            temp = temp.next
            front -= 1
        last = head
        while last.next:
            last = last.next

        last.next = head
        head = temp.next
        temp.next = None
        return head

n = int(input())
array = list(map(int,input().strip().split()))
k = int(input())

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    new = node(ele)
    temp.next = new
    temp = temp.next

ans = ll.kAppend(k,n,ll.head)
ll.printList(ans)
