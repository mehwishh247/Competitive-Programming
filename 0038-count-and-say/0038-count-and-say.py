class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        def solv(n):
            if n==1:
                return "1"

            x=solv(n-1)
            ans=""
    
            i=0
            while i<len(x):
                j=i+1
                cnt_of_i = 1
                while j<len(x) and x[i]==x[j]:
                    cnt_of_i+=1
                    j+=1
                ans+=str(cnt_of_i)+x[i]
                i=j
            return ans
        return solv(n)