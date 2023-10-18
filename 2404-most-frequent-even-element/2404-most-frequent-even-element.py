class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        
        curr = float('-inf')
        ans = float('inf')
        
        
        keys = sorted(cnt.items(), key = lambda x:x[0])
        
        for key,val in keys:
            
            if key % 2 == 0 and val>curr:
                curr = val
                ans = key
                
                
        return ans if ans != float('inf') else -1