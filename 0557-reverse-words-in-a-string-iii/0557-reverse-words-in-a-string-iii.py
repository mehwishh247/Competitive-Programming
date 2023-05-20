class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        arr = s.split(" ")
        
        for x in arr:
            res+=" "+x[::-1]
        return res[1:]
        