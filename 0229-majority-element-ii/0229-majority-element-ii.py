class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        cnt = Counter(nums)
        
        curr = []
        
        for key,val in cnt.items():
            
            if cnt[key]>int(n/3):
                curr += [key]
                
        return curr