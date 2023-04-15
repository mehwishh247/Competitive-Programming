class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i,j,n=0,0,len(chars)
        
        s=""
            
        while i<n:
            while j<n and chars[i]==chars[j]:
                j+=1
            s+=chars[i]
            
            if j-i !=1:
                s+=str(j-i)
            i=j
            
        for x in range(len(s)):
            chars[x]=s[x]

        
        return len(s)
        