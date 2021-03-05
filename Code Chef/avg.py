cases = int(input())
while cases:
    cases -= 1
    num = int(input())
    arr = list(map(int, input().split()))

    if len(set(arr)) == 1 or sorted(arr, reverse=True) == arr:
        print("No")
    else:
        print("Yes")