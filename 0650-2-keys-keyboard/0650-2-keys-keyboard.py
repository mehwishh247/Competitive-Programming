class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        # create a dp array to store the minsteps from 1 to n.
        dp = [0] * (n + 1)
        dp[2] = 2
        for i in range(3, n + 1):
            # find the largest prime factors for every i.
            primefactor = self.primefactor(i)
            # applying step 2 here
            if primefactor == i:
                dp[i] = primefactor
            # applying step 3 here
            else:
                dp[i] = dp[primefactor] + dp[i // primefactor]
        return dp[n]

    # code to find largest prime factor
    def primefactor(self, n: int) -> int:
        res = 2
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                res = i
                n //= i
        if n > 1:
            res = max(res, n)
        return res