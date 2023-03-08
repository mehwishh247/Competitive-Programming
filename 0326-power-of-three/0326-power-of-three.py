class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        if val ==0:
            return True
        if Val%3!=0:
            return False
        
        
        '''
        def solve(val):
            if val==1:
                return True
            if val%3!=0:
                return False
            check = solve(val/3)

            return check
        if n<=0:
            return False
        return solve(n)
        
      