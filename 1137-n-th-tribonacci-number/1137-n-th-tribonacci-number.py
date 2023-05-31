class Solution:
    def tribonacci(self, n: int) -> int:
        
        @cache        
        def fib(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            

            
            ans = fib(n-3)+fib(n-2)+fib(n-1)
    
            return ans
        
        return fib(n)
        