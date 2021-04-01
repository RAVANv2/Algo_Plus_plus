

N,H,x = list(map(int,input().strip().split()))

time = list(map(int,input().strip().split()))

if x >= H:
    print("YES")
else:
    if max(time) + x - H >= 0:
        print("YES")
    else:
        print("NO")