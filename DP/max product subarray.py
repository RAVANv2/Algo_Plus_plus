# Question: https://leetcode.com/problems/maximum-product-subarray/

nums = [2,3,-2,4]

max_prev = nums[0]
min_prev = nums[0]

max_n = nums[0]
min_n = nums[0]

ans = nums[0]

for i in nums[1:]:
    max_n = max(i,max_prev*i,min_prev*i)
    min_n = min(i,max_prev*i,min_prev*i)

    max_prev = max_n
    min_prev = min_n

    ans = max(ans,max_n)

print(ans)
