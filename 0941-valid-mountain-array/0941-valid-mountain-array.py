class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)==1:
            return False
        if arr[0]>arr[1]:
            return False
        
        Result= []
        
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]: return False
            
            if arr[i]<arr[i+1]:
                Result.append(0)
            else:
                Result.append(1)
        print(Result)
        if sorted(Result)==Result  and 0 in Result and 1 in Result:
            return True
        return False
                
                