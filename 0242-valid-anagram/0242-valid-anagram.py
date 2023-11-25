class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # t --> s = True else False
        # can we rearrage s and use it's elements once then get t
        
        if len(s) != len(t): return False
        
        sorted_t = sorted(t)
        sorted_s = sorted(s)

        for i in range(len(t)):
            
            if sorted_t[i]!=sorted_s[i]:
                return False
        return True
            
        
        