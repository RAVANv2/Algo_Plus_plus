
# Given 2 sorted linked lists , merge the two given sorted linked list and print the final Linked List. 

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

    def merge(self,head1, head2):
        new = linkedList()
        new.head = node(-1)
        temp = new.head
        while True:
            if head2 and head1 and head1.data >  head2.data :
                ele = node(head2.data)
                temp.next = ele
                head2 = head2.next
            elif head2 and head1 and head1.data < head2.data:
                ele = node(head1.data)
                temp.next = ele
                head1 = head1.next
            else:
                break
            temp = temp.next
        while head1:
            ele = node(head1.data)
            temp.next = ele
            temp = temp.next
            head1 = head1.next
        while head2:
            ele = node(head2.data)
            temp.next = ele
            temp = temp.next
            head2 = head2.next
        return new.head.next

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        l1 = int(input())
        array1 = list(map(int,input().strip().split()))
        ll1 = linkedList()
        ll1.head = node(array1.pop(0))
        temp = ll1.head
        for ele in array1:
            new = node(ele)
            temp.next = new
            temp = temp.next

        l2 = int(input())
        array2 = list(map(int, input().strip().split()))
        ll2 = linkedList()
        ll2.head = node(array2.pop(0))
        temp = ll2.head
        for ele in array2:
            new = node(ele)
            temp.next = new
            temp = temp.next

        ans = ll1.merge(ll1.head, ll2.head)
        ll1.printList(ans)
