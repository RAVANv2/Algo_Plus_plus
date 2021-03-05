

t = int(input())

while t:

    t -= 1

    a = list(map(int,input().strip().split()))
    k = int(input())

    for i in range(len(a)-1,-1,-1):
        if a[i] - k >= 0 and k>0:
            temp = a[i]
            a[i] = temp - k
            k = k - temp

        elif a[i] - k < 0 and k>0:
            temp = a[i]
            a[i] = 0
            k = k - temp


    for i in range(len(a)-1,-1,-1):
        if a[i] != 0:
            print(i+1)
            break
