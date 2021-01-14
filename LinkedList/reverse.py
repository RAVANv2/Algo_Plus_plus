

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self,head):
        while head:
            print(head.data, end=' ')
            head = head.next

    # Using Recursive method
    def reverse(self, head):

        if head == None:
            return head
        if head.next == None:
            return head
        node = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return node


array = list(map(int,input().strip().split()))

ll = linkedList()
ll.head = node(array.pop(0))
temp = ll.head
for ele in array:
    new = node(ele)
    temp.next = new
    temp = temp.next

ans = ll.reverse(ll.head)

ll.printList(ans)
