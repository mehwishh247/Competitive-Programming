class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        
        def fibDP(n):

            if n<2:
                return n+1
            
            if memo[n]:
                return memo[n]

            ans = fibDP(n-1)+fibDP(n-2)
            memo[n]=ans

            return ans
        
        return fibDP(n-1)