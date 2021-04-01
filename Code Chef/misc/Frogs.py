import math
t = int(input())

while t:
    t -= 1

    n = int(input())
    w = list(map(int, input().strip().split()))
    l = list(map(int, input().strip().split()))

    steps = 0
    newIndex = {}
    for i in range(1,n+1):

        newIndex[i] = w.index(i)

    for i in range(2,n+1):
        var1 = newIndex[i]
        var2 = newIndex[i-1]
        temp = 0
        if var1 <= var2:
            temp = (math.ceil((var2 + 1 - var1)/l[var1]))
        steps += temp

        newIndex[i] += temp*(l[var1])

    print(steps)



