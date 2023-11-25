class Solution:
    
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9"))
    
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        left,right = 0 , n-1
        
        while left<right:
            
            while left<right and not self.alphanum(s[left]):
                left+=1
            while right>left and not self.alphanum(s[right]):
                right-=1
            
            if s[left].lower()!=s[right].lower(): return False
            
            left+=1
            right-=1 
    
            
        return True
 
        
        