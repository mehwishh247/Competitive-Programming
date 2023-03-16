class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def recSol(idx,summ,array):
            if summ>target:
                return 
            if summ==target:
                ans.append(array.copy())
                return 
            visited = set()
            for i in range(idx,len(candidates)):
                if candidates[i] not in visited:
                    visited.add(candidates[i])
                    summ+=candidates[i]
                    array.append(candidates[i])
                    recSol(i+1,summ,array)
                    out = array.pop()
                    summ-=out 
                    
        recSol(0,0,[])
        return ans
                
               


