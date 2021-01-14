# Arrange elements in a Linked List such that all even numbers are placed after odd numbers.

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

    def evenAfterOdd(self,head):
        temp = head
        newList = linkedList()
        newList.head = node(-1)
        point =  newList.head
        while temp:
            if temp.data % 2:
                new = node(temp.data)
                temp.data = temp.data*-1
                point.next = new
                point = point.next
            temp = temp.next
        temp = head
        while temp:
            if temp.data > 0:
                new = node(temp.data)
                point.next = new
                point = point.next
            temp = temp.next

        return newList.head.next

n = int(input())
array = list(map(int, input().strip().split()))

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    new = node(ele)
    temp.next = new
    temp = temp.next

ans = ll.evenAfterOdd(ll.head)

ll.printList(ans)