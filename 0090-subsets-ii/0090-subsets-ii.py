class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set() 
        temp = []
        
        
        def soln(indx):
            pos = temp[:]
            pos.sort()
            ans.add(tuple(pos))
            for i in range(indx,len(nums)):
                temp.append(nums[i])
                soln(i+1)
                temp.pop()
                
        soln(0)
        
        return ans