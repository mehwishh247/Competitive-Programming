class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        candidates = [x for x in range(1,10)]
        self.sum = 0
        target = n
        
        def recSol(idx,array):
            if self.sum==target and len(array)==k:
                ans.append(array.copy())
                return 
        
            if idx>=len(candidates) or self.sum>target or target-self.sum < candidates[idx]:
                return 

            visited = set()
            for i in range(idx,len(candidates)):
                if candidates[i] not in visited:
                    visited.add(candidates[i])
                    self.sum+=candidates[i]
                    array.append(candidates[i])
                    recSol(i+1,array)
                    out = array.pop()
                    self.sum-=out 
                    
        recSol(0,[])
        return ans
                
               