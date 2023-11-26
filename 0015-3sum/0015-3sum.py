class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
         [-4,-1,-1,0,1,2,-4]
         [-2,0,0,2,2]
         __, __, __
        
        '''
        
        nums.sort()
        n = len(nums)
        
        answer = []
        
        for i in range(n):
            
            
            if i>0 and nums[i-1] == nums[i]: continue
                
            l,r = i+1,n-1
            
            while l<r:
                
                curr_sum = nums[l]+nums[r] + nums[i]
                
                if curr_sum>0:
                    r-=1
                elif curr_sum<0:
                    l+=1
                else:
                    
                    answer.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                    
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
        return answer
                    
                    
                
                
            
        
        