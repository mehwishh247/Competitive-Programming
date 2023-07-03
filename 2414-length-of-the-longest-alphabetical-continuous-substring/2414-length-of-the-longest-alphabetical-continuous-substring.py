class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        ans=1
        
        n=len(s)
        
        
        temp=1
        
        for i in range(n-1):
            if ord(s[i])+1==ord(s[i+1]):
                temp+=1
            else:
                ans=max(ans,temp)
                temp=1
        
        ans=max(ans,temp)
        return ans
    
    