class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
            low,hi=0,len(arr)-1
            
            while low+1 < hi:
                mid = low + (hi-low)//2
                
                if arr[mid-1]>arr[mid] and arr[mid]>arr[mid+1]:
                    hi=mid
                elif arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]:
                    low=mid
                else:
                    return mid
        
                    
                
                
        