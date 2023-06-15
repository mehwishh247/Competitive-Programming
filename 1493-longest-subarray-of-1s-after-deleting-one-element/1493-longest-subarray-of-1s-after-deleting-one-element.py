class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        view = defaultdict(int)
        
        currentLenMax = float('-inf')
        ans=0
        
        n= len(nums)
        
        for i in range(n):
            
            if nums[i]==0:
                
                lefty,righty=i-1,i+1
                
                
                
                while lefty>=0 and nums[lefty]==1:
                    lefty-=1
                while righty<n and nums[righty]==1:
                    righty+=1
                    


                currentLenMax = max(currentLenMax,righty-lefty-2)
                    
                view[i] = righty-lefty-2
        

        if not view:
            return n-1
        return currentLenMax
                
                
        