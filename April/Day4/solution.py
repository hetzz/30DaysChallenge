def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count_of_zeroes = 0
    x = 0
    while x < len(nums):
        if nums[x] == 0:
            nums.remove(nums[x])
            count_of_zeroes += 1
        else:
            x += 1
    for i in range(count_of_zeroes):
        nums.append(0)

nums = [0,0,1]
moveZeroes(nums)
print(nums)