class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=0,x
        
        while low<=high:
            mid= low + (high-low)//2
            sqr = mid*mid
            if sqr==x:
                return mid
            elif sqr<x:
                if (mid+1)**2>x:
                    return mid
                low=mid+1
            else:
                if (mid-1)**2<x:
                    return mid-1
                high=mid-1
                
                
            
        