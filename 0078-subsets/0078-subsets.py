class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        temp = []
        
        def soln(indx):
            
            ans.append(temp[:])
            
            for i in range(indx,len(nums)):
                temp.append(nums[i])
                soln(i+1)
                temp.pop()
        
        soln(0)
        return ans
                
                