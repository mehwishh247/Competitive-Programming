class Solution:
    def findComplement(self, num: int) -> int:
        
            x = num
            mask =1
            while mask<=x:
                x = x ^ mask
                mask= mask << 1
            return x
