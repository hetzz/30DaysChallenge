def findMaxLength(nums):
    hash_map = {}   
    curr_sum = 0 
    max_len = 0 
    ending_index = -1 
    n = len(nums)

    for i in range (0, n):  
        if(nums[i] == 0):  
            nums[i] = -1 
  
    for i in range (0, n):   
        curr_sum = curr_sum + nums[i]  
        if (curr_sum == 0):  
            max_len = i + 1 
            ending_index = i    
        if curr_sum in hash_map: 
            if max_len < i - hash_map[curr_sum]: 
                max_len = i - hash_map[curr_sum] 
                ending_index = i 
        else:  
            hash_map[curr_sum] = i   
          
    for i in range (0, n):  
        if(nums[i] == -1):  
            nums[i] = 0 
        else:  
            nums[i] = 1 
  
    return max_len 

num = [1,0,1]
print(findMaxLength(num))