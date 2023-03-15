class Solution:
    def revInv(self,s):
            result = ""
            for i in range(len(s)):
                if s[i]=="1":
                    result+="0"
                else:
                    result+="1"
            return result[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        
        def recur(n):
            if n==1:
                return "0"
            temp=recur(n-1)    
            ans= temp+"1"+self.revInv(temp)
            
            return ans
       
        x = recur(n)
        return x[k-1]
        
        
      
        