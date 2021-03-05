class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

# This function gets two arguments - the head pointers of the two linked lists
# Return the node which is the intersection point of these linked lists
# It is assured that the two lists intersect
def intersectionOfTwoLinkedLists(l1, l2):
    len1 = 0
    len2 = 0
    temp = l1
    while temp:
        len1 += 1
        temp = temp.next
    temp = l2
    while temp:
        len2 += 1
        temp = temp.next

    if len1 > len2:
        extra = len1 - len2
        while extra:
            l1 = l1.next
            extra -= 1
        while l1 and l2:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
    else:
        extra = len2 - len2
        while extra:
            l2 = l2.next
            extra -= 1

        while l2 and l1:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next
    return None
#
#
#
#
# You do not need to refer or modify any code below this.
# Only modify the above function definition.
# Any modications to code below could lead to a 'Wrong Answer' verdict despite above code being correct.
# You do not even need to read or know about the code below.
#
#
#
#

def buildList(hash):
    l = [int(x) for x in input().split()]
    head = Node(l[0])
    current = head
    hash[l[0]] = head

    for x in l[1:]:
        if x == -1:
            break

        n = Node(x)
        hash[x] = n
        current.next = n
        current = n

    current.next = None
    return head


def printLinkedList(head):
    while head != None:
        print(head.data, end=' ')
        head = head.next
    print()


hash = {}
l1 = buildList(hash)

inpArr = [int(x) for x in input().split()]

x = inpArr[0]
l2 = Node(x)
temp = l2


for x in inpArr[1:]:
    if x == -1:
        break

    if x in hash:
        temp.next = hash[x]
        break

    n = Node(x)
    temp.next = n
    temp = n


print("L1 - ", end=' ')
printLinkedList(l1)
print("L2 - ", end=' ')
printLinkedList(l2)
intersectionPoint = intersectionOfTwoLinkedLists(l1, l2)

print("Intersection at node with data = ", intersectionPoint.data, sep='')
