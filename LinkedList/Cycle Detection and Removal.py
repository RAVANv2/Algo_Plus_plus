class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


# head - Head pointer of the Linked List
# Return a boolean value indicating the presence of cycle
# If the cycle is present, modify the linked list to remove the cycle as well
def floydCycleRemoval(head):
    fast = head
    slow = head
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == None or slow == None:
            return False

        if fast == slow:
            slow = head
            while fast.next != slow.next:
                fast = fast.next
                slow = slow.next
            fast.next = None
            return True

def buildCycleList():
    hash = {}
    inpArr = [int(x) for x in input().split()]
    x = inpArr[0]
    if x == -1:
        head = None
        return head

    head = Node(x)
    hash[x] = head
    current = head
    for x in inpArr[1:]:
        if x == -1:
            break
        if x in hash:
            current.next = hash[x]
            return head
        n = Node(x)
        current.next = n
        current = n
        hash[x] = n

    current.next = None
    return head


def printLinkedList(head):
    s = set()
    while head != None:
        if head.data in s:
            print("\nCycle detected at ", head.data, sep='', end='')
            return
        print(head.data, end=' ')
        s.add(head.data)
        head = head.next


head = buildCycleList()

cyclePresent = floydCycleRemoval(head)
if cyclePresent:
    print("Cycle was present")
else:
    print("No cycle")

print("Linked List - ", end='')
printLinkedList(head)
