class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        himax = 0
        for i in range(len(nums)-1):
            if i > himax:
                return False
            else:
                if i+nums[i] >= len(nums)-1:
                    return True
                if i+nums[i] > himax:
                    himax = i+nums[i]
        return False

'''
Other approach
public class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        return lastPos == 0;
    }
}
'''