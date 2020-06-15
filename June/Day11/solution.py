class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        twos = 0
        for i in nums:
            if i == 1:
                ones+= 1
            elif i == 2:
                twos+= 1
        zeros = len(nums) - ones - twos
        for i in range(len(nums)):
            if zeros:
                nums[i] = 0
                zeros -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2