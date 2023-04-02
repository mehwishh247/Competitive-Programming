class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        in_state = n&1
        n= n>> 1
        while n>0:
            state = n&1
            if in_state == state:
                return False
            in_state = state
            n= n>> 1
        return True
