class Solution:
        def findKthBit(self, n: int, k: int) -> str:
            
            def solver(n,k):
                if n==1:
                    return 0
                
                size = 2**n-1
                
                if k<size//2+1:
                    return solver(n-1,k)
                elif k>size//2+1:
                    backsize = 2**(n-1)-1 
                    gap = k-(size//2+1)
                    return 1-solver(n-1,backsize-gap+1)
                else:
                    return 1
                    
            return str(solver(n, k))


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     def revInv(self,s):
#             result = ""
#             for i in range(len(s)):
#                 if s[i]=="1":
#                     result+="0"
#                 else:
#                     result+="1"
#             return result[::-1]
    
    # def findKthBit(self, n: int, k: int) -> str:
        
#         def recur(n):
#             if n==1:
#                 return "0"
#             temp=recur(n-1)    
#             ans= temp+"1"+self.revInv(temp)
            
#             return ans
       
#         x = recur(n)
#         return x[k-1]
        
        
      
        