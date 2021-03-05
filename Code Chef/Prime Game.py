

t = int(input())



boolArr = [True for _ in range(1000001)]
boolArr[0] = boolArr[1] = False

i = 2
while i*i <= 1000000:
    if boolArr[i]:
        for j in range(i*i,1000000,i):
            boolArr[j] = False
    i += 1

dp = [0 for _ in range(1000001)]

for i in range(1,1000000):
    if boolArr[i]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]


while t:
    t -= 1
    X,Y = list(map(int, input().strip().split()))

    if dp[X] > Y:
        print("Divyam", end='\n')
    else:
        print("Chef", end='\n')