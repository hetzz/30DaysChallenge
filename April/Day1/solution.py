class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for i in nums:
            if num_dict.get(i):
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        
        key_list = list(num_dict.keys()) 
        val_list = list(num_dict.values()) 
  
        return key_list[val_list.index(1)]