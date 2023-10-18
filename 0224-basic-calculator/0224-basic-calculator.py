class Solution:
    def calculate(self, s: str) -> int:
        
        # Input: s = "(1+(4+5+2)-3)+(6+8)"
        # Output: 23
        
        '''
            "(3-(5-8-13-4))"
            
        
        '''
        
        
        s = s.replace(" ",'')
        stack = []
        
        for i,ltr in enumerate(s): #  3 * 10^5

            # print(stack)
            if ltr == ")":
                temp = "" 
                while stack[-1] != "(":  # 3 * 10^5 
                    val = stack.pop()
                    
                    if len(val) > 1:
                        val = val[::-1]
                    
                    temp += val

                    
                stack.pop()
                stack.append(str(eval(temp[::-1])))
                
            else:
                stack.append(ltr)
        
        return eval("".join(stack))