class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def solve(n):
            if n==1:
                return True

            if n%4!=0:
                return False
            return self.isPowerOfFour(n/4)
        if n<=0:
            return False
        return solve(n)

