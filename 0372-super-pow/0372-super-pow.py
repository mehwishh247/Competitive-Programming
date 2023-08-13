class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        power = int("".join(map(str,b)))
        ans = pow(a,power,1337)
        
        return ans