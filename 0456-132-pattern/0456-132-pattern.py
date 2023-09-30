class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        third = float("-inf")
        stack = []
        
        for curr in nums[::-1]:
            
            if curr < third:
                return True
            
            while stack and curr > stack[-1]:
                third  = stack.pop()
            
            stack.append(curr)
        
        return False
            
            
