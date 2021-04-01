


t = int(input())

def greater(idx):
    for ele in idx:
        if ele[1] > ele[0]:
            return True
    return False


while t:
    t -= 1

    n = int(input())

    a = list(map(int,input().strip().split()))

    a = sorted(a)

    idx = []

    for i in range(1,n+1):
        idx.append([i,a[i-1]])

    if greater(idx):
        print("Second")
    else:
        diff = 0
        for ele in idx:
            diff += abs(ele[0] - ele[1])

        if diff % 2 == 0:
            print("Second")
        else:
            print("First")


