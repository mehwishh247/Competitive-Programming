class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [0,3,7,2,5,8,4,6,0,1]
        counts = Counter(nums) # 0:2, 1:1 2:1 3:1 4:1 5:1 6:1 7:1 8:1
        
        curr_max = 0
        
        for i in range(len(nums)):
            
            temp = 1
            need = nums[i]+1
            
            if nums[i]-1 in counts: continue
                
            
            while counts[need]:
                
                temp += 1
                need += 1
            
            curr_max = max(curr_max,temp)
            
        return curr_max
            
            
            