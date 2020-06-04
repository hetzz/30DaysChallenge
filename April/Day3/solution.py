def maxSubArray(nums):
    f = [0 for i in range(len(nums))]
    maxsum, f[0] = nums[0],nums[0]
    for i in range(1,len(nums)):
        f[i] = max(nums[i],f[i-1] + nums[i])
        maxsum = max(maxsum,f[i])
    return maxsum

nums = [1]
print(maxSubArray(nums))