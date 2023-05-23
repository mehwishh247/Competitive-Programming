class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans=set()
        used =set()
        n=len(nums)
        
        temp=[]
        
        def soln():

            
            if len(temp)==n:
                ans.add(tuple(temp))
            
                
            for i in range(n):
                
                if i not in used:
                    used.add(i)

                    temp.append(nums[i])
                    soln()
                    temp.pop()
                    used.discard(i)
                
        soln()
        return ans