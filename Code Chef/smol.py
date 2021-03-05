

t = int(input())

while t:

    t -= 1

    N,K = list(map(int,input().strip().split()))

    if N<K:
        print(N)

    elif K==0:
        print(N)

    else:
        ans = N % K
        print(ans)