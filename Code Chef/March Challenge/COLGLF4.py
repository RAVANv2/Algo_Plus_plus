


def minCost(n,e,h,a,b,c):
    ans = float("inf")

    if n <= 0:
        return 0

    if n <= e and n <=h:
        ans = min(ans,n*c)

    if 2*n<=e:
        ans = min(ans,n*a)

    if 3*n <= h:
        ans = min(ans,n*b)

    if n<=e and n<=h:
        ans = min(ans,n*c)

    if ((h-n)//2 >= 1) and ((h-n)//2 >= n-e):
        if b-c<0:
            k = min(n-1,(h-n)//2)
            ans = min(ans,(b-c)*k+n*c)
        else:
            k = max(1,n-e)
            ans = min(ans,(b-c)*k+n*c)

    if ((e-n)>=1 and (e-n)>=n-h):
        if (a-c)<0:
            k = min(n-1,(e-n))
            ans = min(ans,(a-c)*k+n*c)
        else:
            k = max(1,n-h)
            ans = min(ans,(a-c)*k+n*c)
    if ((e//2>=1) and (e//2>=(3*n-h+2)//3)):
        if a-b<0:
            k = min(n-1,(e//2))
            ans = min(ans,(a-b)*k+n*b)
        else:
            k = max(1,(3*n-h+2)//3)
            ans = min(ans,(a-b)*k+n*b)
    if (e>=3 and h>=4 and n>=3):
        ans = min(ans, a+b+c+minCost(n-3,e-3,h-4,a,b,c))

    return ans


t = int(input())

while t:
    t -= 1

    n,e,h,a,b,c = list(map(int,input().strip().split()))

    ans = minCost(n,e,h,a,b,c)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)