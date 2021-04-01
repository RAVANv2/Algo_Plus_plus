

t = int(input())

while t:
    t -= 1

    N,M = list(map(int,input().strip().split()))

    ans = []
    for row in range(N):
        rec = "0"
        grid = input().strip()

        for idx in range(len(grid)):
            if grid[idx] == "1":
                rec += str(idx)

        if rec != "0":
            ans.append(int(rec))


    if max(ans) - min(ans) == 0:
        print("YES")
    else:
        print("NO")
