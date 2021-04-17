class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        fnum = ""
        while first:
            fnum += str(first.data)
            first = first.next
        snum = ""
        while second:
            snum += str(second.data)
            second=second.next
        ans = str(int(fnum)+int(snum))
        i = 0
        head = Node(-1)
        ptr = head
        while i < len(ans):
            head.next =  Node(ans[i])
            head = head.next
            i += 1
        return ptr.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
