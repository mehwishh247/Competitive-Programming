class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for x in s:
            if x=="(" or x=="[" or x=="{":
                stack.append(x)
            else:
                if len(stack)>0 and dic[x]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
                    
                
                
            
            
            
            
            #         go through every element
# check if it is the opening and if it is add it to the stack
# if it is closing check if the opening of the that element is in the stack
# if its opening is in the stack pop the stack
# if not break and return false
        
            
