class Solution:
    def findComplement(self, num: int) -> int:
        
            # x = num
            # mask =1
            # while mask<=x:
            #     x = x ^ mask
            #     mask= mask << 1
            # return x
            mask_len=len(bin(num))-2
            mask='1' * mask_len
            mask_n=int(mask,2)
            return num ^ mask_n
        
