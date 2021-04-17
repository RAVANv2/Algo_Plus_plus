
arr = [1, 101, 2, 3, 100, 4, 5]
dp = [0]*len(arr)
for i in range(len(arr)):
    dp[i] = arr[i]

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(dp)
print(max(dp))