class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        minn = min(arr)
        i=0
        while i<len(arr):
            if arr[i]-minn==i:
                i+=1
            else:
                temp = arr[i]-minn
                if temp>=len(arr)-1:
                    i+=1
                    continue
                arr[i],arr[temp] = arr[temp], arr[i]
        
        for i in range(len(arr)):
            if i!=arr[i]:
                return i
        return i+1
