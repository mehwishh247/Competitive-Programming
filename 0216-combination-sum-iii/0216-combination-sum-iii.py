class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        candidates = [x for x in range(1,10)]
        target = n
        def recSol(idx,summ,array):
            if summ==target and len(array)==k:
                ans.append(array.copy())
                return 
        
            if idx>=len(candidates) or summ>target or target-summ < candidates[idx]:
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
                
               