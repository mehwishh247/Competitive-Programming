class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        melse = sorted(list(set(arr)))
        
        ranks = {el:i for i,el in enumerate(melse)}
        
            
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]+1
        
        return arr        