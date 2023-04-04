class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        stack = []
        used=set()
        def recSol():
            n=len(nums)
            if len(stack)==n:
                ans.append(stack.copy())
                return 
            
            for i in range(n):
                if i not in used:
                    used.add(i)     
                    stack.append(nums[i])                   
                    recSol()
                    used.discard(i)     
                    stack.pop()    
    
            

                    
        recSol()
        return ans