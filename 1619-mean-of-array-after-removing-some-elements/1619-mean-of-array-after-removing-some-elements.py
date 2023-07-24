class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        n = len(arr)
        arr.sort()
        
        start =  int(n*0.05)
        end = int(n*0.95)
        
        total = 0
        
        for i in range(start,end,1):
            total+=arr[i]
            
        return total/(end-start)
