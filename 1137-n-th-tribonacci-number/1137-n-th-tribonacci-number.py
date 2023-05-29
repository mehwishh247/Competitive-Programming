class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo=defaultdict(int)
        
        def fib(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            
            if memo[n]:
                return memo[n]
            
            ans = fib(n-3)+fib(n-2)+fib(n-1)
            
            memo[n]=ans
            
            return ans
        
        return fib(n)
        