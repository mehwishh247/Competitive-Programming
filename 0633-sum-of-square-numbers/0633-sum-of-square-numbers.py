class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        limit = int(c**0.5)+1
        for i in range(0,limit):  
            num = c-i**2
            if num**0.5==int(num**0.5):
                return True
            
        return False
            
                