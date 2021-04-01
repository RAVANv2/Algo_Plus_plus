
import bisect

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

n = len(startTime)

startTime, endTime, profit = (list(x) for x in zip(*sorted(zip(startTime, endTime, profit))))

dp = [0]*n

print(startTime, endTime, profit)

dp[-1] = profit[-1]
for i in range(n-2, -1,-1):
    j = bisect.bisect_left(startTime, endTime[i])
    print((j,endTime[i]),end=" ")
    dp[i] = max(profit[i] + dp[j] if j < n else profit[i], dp[i+1])
print()
print(dp)
print(dp[0])

