class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def recSol(idx,summ,array):
            if summ>target:
                return 
            if summ==target:
                array = array.copy()
                ans.append(array)
                return
                
            for i in range(idx,len(candidates)):
                summ+=candidates[i]
                array.append(candidates[i])
                recSol(i,summ,array)
                out = array.pop()
                summ-=out   
        recSol(0,0,[])
        return ans
                
                
        