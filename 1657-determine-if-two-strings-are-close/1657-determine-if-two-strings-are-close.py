class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        len1,len2 = len(word1),len(word2)
        if len1!=len2:return False
        
        got,need = Counter(word1),Counter(word2)       
        
        if set(got.keys()) != set(need.keys()): return False
        
        if sorted(got.values()) != sorted(need.values()): return False
        

        return True