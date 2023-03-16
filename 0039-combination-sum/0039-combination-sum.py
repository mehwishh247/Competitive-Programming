class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        candidates.sort()
        def recSol(idx,summ,array):
            if summ>target:
                return 
            if summ==target:
                array = array.copy()
                self.ans.append(array)
                return
                
            for i in range(idx,len(candidates)):
                summ+=candidates[i]
                array.append(candidates[i])
                recSol(i,summ,array)
                out = array.pop()
                summ-=out   
        recSol(0,0,[])
        return self.ans
                
                
        