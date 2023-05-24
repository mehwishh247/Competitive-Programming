class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sorted_arr = sorted(costs, key=lambda x: x[0] - x[1])
        
        ans=0
        n=len(costs)
        
        for i,ele in enumerate(sorted_arr):
            if i<(n//2):
                ans+=ele[0]
            else:
                ans+=ele[1]        
        
        return ans