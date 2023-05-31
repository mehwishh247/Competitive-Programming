class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0
        
        arr= [0,1]
        
        for i in range(1,n):
            arr.append(arr[-1]+arr[-2])

            
        return arr[-1]
        