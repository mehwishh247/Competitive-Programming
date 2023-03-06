class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        Llength,Slength= len(s),len(p)
        result = []
        p=sorted(p)
        for i in range(0,Llength-Slength+1):
            if sorted(s[i:i+Slength])==p:
                result.append(i)
        return result
        