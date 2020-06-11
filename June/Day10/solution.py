class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l,r)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            else:
                if target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
        if target < nums[0]:
            return 0
        return l                                                                                                            
        