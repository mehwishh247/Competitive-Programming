class Solution:
    def calculate(self, s: str) -> int:
        
        num = ''
        eqn =[]
        
        oprts = {"/","*","-","+"}
        
        for i,ltr in enumerate(s):
            if ltr not in oprts:
                if ltr != " ":
                    num += ltr
                
            else:
                eqn.extend([num,ltr])
                num = ''
                
            if i == len(s) - 1:
                eqn.append(num)

        stack = []
        n = len(eqn)
        
        j = 0
        while j<n:
            
            ckr = eqn[j]
            if stack and stack[-1] in ["/","*"]:
        
                opt = stack.pop()
                num = stack.pop()

                res = int(eval(num+opt+ckr))
                stack.append(str(res))
                
                j+=1
                continue
             
            stack.append(ckr)
            j += 1


        return eval("".join(stack))
                
                