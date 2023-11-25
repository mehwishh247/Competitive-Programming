class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        preffix = [0]*n
        preffix[0] = nums[0]
        
        for i in range(n):
            preffix[i] = preffix[i-1]*nums[i] if i-1>-1 else nums[i]
            
        answer = [0]*n
        
        for i in range(n-1,0,-1):
            
            if i==n-1: answer[i] = preffix[i-1] 
            
            else:
                answer[i] = preffix[i-1] * nums[i+1]
                nums[i] *= nums[i+1]
            
        answer[0] = nums[1] 
            
        return answer