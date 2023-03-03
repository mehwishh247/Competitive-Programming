# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high=1,n
        
        while low<=high:
            mid=low + (high-low)//2
            if isBadVersion(mid):
                if mid==1 or not isBadVersion(mid-1):
                    return mid
                high=mid-1
            else:
                if isBadVersion(mid+1):
                    return mid+1
                low=mid+1
                    
                
        
#         if bad the right is ignored
#         if good move to the right 
#   what is my return cased 