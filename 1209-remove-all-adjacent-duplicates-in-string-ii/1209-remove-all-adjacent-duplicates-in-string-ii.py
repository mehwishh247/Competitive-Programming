class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # "deeedbbcccbdaa"
        stack = [("!",0)]
        
        for i,ltr in enumerate(s):
            
            if stack[-1][0]!=ltr:
                stack.append((ltr,1))
                continue
                
            if stack[-1][-1]==k-1:
                
                while stack and stack[-1][0]==ltr:
                    stack.pop()
            
            else:
                
                prev = stack[-1][-1]
                stack.append((ltr,prev+1))
        
        result = [x[0] for x in stack] 
        
        return "".join(result)[1::]
        
                
                