class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        def recSol(candidates,summ,array):
            if summ>target:
                return 
            if summ==target:
                array = array.copy()
                self.ans.append(array)
                return
                
            for i in range(len(candidates)):
                summ+=candidates[i]
                array.append(candidates[i])
                recSol(candidates[i::],summ,array)
                out = array.pop()
                summ-=out   
        recSol(candidates,0,[])
        
        return self.ans
                
                
        