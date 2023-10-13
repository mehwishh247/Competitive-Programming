class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for i,ltr in enumerate(s):
            if not stack or stack[-1]!=ltr:
                stack.append(ltr)
            else:
                stack.pop()
        
        
        return  "".join(stack)