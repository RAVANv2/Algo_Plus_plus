
class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def inserAtHead(self, data):
        new = node(data)
        new.next = self.head
        self.head = new

    def inserAtEnd(self, data):
        new = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def inserAtMiddle(self, data, index):
        new = node(data)
        temp = self.head
        while index:
            temp = temp.next
            index -= 1
        new.next = temp.next
        temp.next = new



if __name__ == "__main__":

    get = list(map(int,input().strip().split()))

    # Making a list of with single element
    li = linkedList()
    li.head = node(get.pop(0))
    temp = li.head

    # Adding all the elements in linkedList
    for ele in get:
        new_temp = node(ele)
        temp.next = new_temp
        temp = temp.next
 
    li.inserAtHead(1)
    li.inserAtEnd(6)
    li.inserAtMiddle(4,2)

    temp = li.head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next

