class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        i=0
        for key in count.keys():
            if count[key]>=2:
                nums[i]=key
                nums[i+1] = key
                i+=2
            else:
                nums[i]=key
                i+=1
            
        
        # print(nums)
        
        return i
        
        