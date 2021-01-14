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

n = int(input())
array = list(map(int, input().strip().split()))

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    new = node(ele)
    temp.next = new
    temp = temp.next

ll.printList(ll.head)