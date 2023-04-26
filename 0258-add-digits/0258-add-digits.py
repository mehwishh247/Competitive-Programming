class Solution:
    def addDigits(self, num: int) -> int:
        
        nm = num
        while nm>9:
            nm= sum(map(int,list(str(nm))))
        return nm