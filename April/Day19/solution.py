def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] <= nums[high]:
            if( target > nums[mid]) & (target <= nums[high]):
                low = mid + 1
            else:
                high = mid - 1
        else:
            if (nums[low] <= target) & (target < nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))