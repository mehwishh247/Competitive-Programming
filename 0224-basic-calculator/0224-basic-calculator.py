class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(" ",'')
        stack = []
        
        for i,ltr in enumerate(s): 

            if ltr == ")":
                temp = "" 
                while stack[-1] != "(": 
                    val = stack.pop()
                    
                    if len(val) > 1:
                        val = val[::-1]
                    
                    temp += val

                    
                stack.pop()
                stack.append(str(eval(temp[::-1])))
                
            else:
                stack.append(ltr)
        
        return eval("".join(stack))