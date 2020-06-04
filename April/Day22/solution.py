def subarraySum(nums,k):
    sum_array = []
    result = 0
    sum_array.append(0)
    for n in range(len(nums)):
        sum_array.append(sum_array[n] + nums[n])
    print(sum_array)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            if k == sum_array[j] - sum_array[i]:
                result += 1
    return result

nums = [1,1,1]
k = 2
print(subarraySum(nums,k))
'''
Alternate hash table solution
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}

'''