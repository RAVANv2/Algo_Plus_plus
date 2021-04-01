

nums = [20,8,27,37,9,12,46]

def maxSum(nums):
        dp = [0]*(len(nums))

        for i in range(len(nums)):
            dp[i] = nums[i]

        for i in range(1,len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]) and (dp[i] < dp[j]+nums[i]):
                    dp[i] = dp[j]+nums[i]

        print(dp)
        return max(dp)

print(maxSum(nums))
