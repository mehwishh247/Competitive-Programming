class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        '''
            4 2 1 8  5 2 
            
            "8,5,2"
        
        '''
        stack = []
        
        n = len(nums)
        
        answer = [-1]*n
        
        for i in range(n):
            
            while stack and stack[-1][0]< nums[i]:
                
                num,index = stack.pop()
                
                answer[index] = nums[i]
            
            stack.append((nums[i],i))
        
        
        for i in range(n):
            
            
            while stack and stack[-1][0]< nums[i] and answer[stack[-1][-1]]==-1:
                
                
                num,index = stack.pop()
                
                answer[index] = nums[i]
            
            
            
            
            
        return answer
                
                
        
        