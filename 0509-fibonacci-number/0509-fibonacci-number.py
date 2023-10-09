class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        
        nminus1,nminus2 = 0,1
        
        for i in range(1,n):
            
            answer = nminus1+nminus2
            nminus1 = nminus2
            nminus2 = answer
        
        return nminus2
        