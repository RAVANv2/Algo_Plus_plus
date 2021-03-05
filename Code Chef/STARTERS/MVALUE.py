

t = int(input())

def findMax(arr):
    arr = sorted(arr)

    one = arr[0]*arr[1] + max(arr[0]-arr[1],arr[1]-arr[0])

    two =arr[-1]*arr[-2] + max(arr[-1] - arr[-2],arr[-2]-arr[-1])

    return max(one,two)

while t:

    t -= 1

    n = int(input())

    arr = list(map(int,input().strip().split()))

    print(findMax(arr))


