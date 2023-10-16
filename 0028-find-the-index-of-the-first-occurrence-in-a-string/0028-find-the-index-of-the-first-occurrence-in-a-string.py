class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        try:
            Pos = haystack.index(needle)
            return Pos
        except:
            return -1
