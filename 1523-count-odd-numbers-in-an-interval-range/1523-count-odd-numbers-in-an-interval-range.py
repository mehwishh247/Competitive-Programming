class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=0
        if low%2:
            c+=1
            low+1
        if high%2:
            c+=1
            high-=1
        c+=(high-low)//2
        return c
            
        