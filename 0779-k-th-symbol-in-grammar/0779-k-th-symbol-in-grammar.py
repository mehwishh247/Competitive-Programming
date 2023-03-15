class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def solver(n,k):
            if n==1:
                return 0
            
            if k%2:
                newK=k//2+1
                return solver(n-1,newK)
            newK = k//2
            return  1-solver(n-1,newK)
            
        return solver(n,k)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def solver(n):
#             if n==1:
#                 return "0"

#             ans = solver(n-1)

#             result=""
#             for i in range(len(ans)):
#                 if ans[i]=="0":
#                     result+="01"
#                 else:
#                     result+="10"


#             return result

#         build = solver(n)

#         return int(build[k-1])

