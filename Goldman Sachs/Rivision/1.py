




if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = list(map(int,input().strip().split()))

        ans1 = ans2 = 0

        for i in range(n):
            if not i%2:
                ans1 += a[i]
            else:
                ans2 += a[i]

        print(max(ans1,ans2))
