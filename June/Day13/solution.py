class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) <= 1:
            return nums
        subset = []
        nums.sort()
        dp = [1 for i in range(len(nums))]
        maxl = 1
        l = len(nums)
        for i in range(1,l):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1+ dp[j]
                    maxl = max(maxl,dp[i])        
        
        for i in range(l-1,-1,-1):
            if dp[i] == maxl:
                subset.append(nums[i])
                maxl -= 1
        return subset
        