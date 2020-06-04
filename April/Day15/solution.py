def productExceptSelf(nums):
    prod = [1 for i in range(len(nums))]
    prod[0] = 1
    for i in range(1,len(nums)):
        prod[i] = prod[i-1] * nums[i-1]
    R = 1
    for i in range(len(nums)-1,-1,-1):
        prod[i] = prod[i] * R
        R *= nums[i]
    return prod

nums = [1,2,3,4]
print(productExceptSelf(nums))