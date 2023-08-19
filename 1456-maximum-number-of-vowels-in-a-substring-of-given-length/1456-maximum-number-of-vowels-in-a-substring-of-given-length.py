class Solution:
    
    def isVowel(self,a):
          return (a == "a" or a == "e" or a == "i" or a == "o" or a == "u")
            
    def maxVowels(self, s: str, k: int) -> int:
        
        n = len(s)
        vowelCout = 0

        
        for i in range(k):
            if self.isVowel(s[i]):
                vowelCout +=1
        
        # print(vowelCout,n)
        maxVowel = vowelCout
        for i in range(k,n):
            
            if self.isVowel(s[i]):
                vowelCout+=1
            
            if self.isVowel(s[i-k]):
                vowelCout-=1
            
            maxVowel = max(maxVowel,vowelCout)
                
            
        return maxVowel
    
        
 
        
        
        
        