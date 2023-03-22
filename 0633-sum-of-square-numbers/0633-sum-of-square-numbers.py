class Solution:
    def isPerfectSquare(self, num):
        if num**0.5==int(num**0.5):
            return True
        return False
    
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(c**0.5)+1
        for i in range(0,limit):  
            if self.isPerfectSquare(c-i**2):
                return True
            
        return False
            
                