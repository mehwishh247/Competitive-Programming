class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # t --> s = True else False
        # can we rearrage s and use it's elements once then get t
        
        if len(s) != len(t): return False
        
        countT,countS = Counter(t),Counter(s)
        
        return countT==countS
            
            