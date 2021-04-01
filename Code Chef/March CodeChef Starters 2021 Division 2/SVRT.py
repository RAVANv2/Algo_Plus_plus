import sys



#  Not done
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def possible(mid,n,k):
    i = 1
    k -= 1
    while i + mid<= n and k:
        k -= 1
        i += mid
    if abs(i - n) == k or k == 0:
        return True
    else:
        return False
t = int(input())

while t:
    t -= 1
    n,k = list(map(int,input().strip().split()))

    start = 2
    end = n

    idx = -1
    while start <= end:
        mid = (start + end) // 2
        if possible(mid,n,k):
            idx = mid
            start = mid + 1
        else:
            end = mid - 1

    print(idx)
    # print(ans)
    # final = {}
    # for key in ans:
    #     count = 0
    #     for ser in range(len(ans[key])-1):
    #         if abs(ans[key][ser] - ans[key][ser+1]) == key:
    #             count += 1
    #     final[key] = count
    #
    # print(final)