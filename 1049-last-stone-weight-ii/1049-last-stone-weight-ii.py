class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = ceil(total/2)
        
        
        @cache
        def dfs(idx,dimr):
            if idx > len(stones)- 1 or dimr >= target:
                return abs(total - 2 * dimr)
            return min(dfs(idx+1,dimr+stones[idx]),dfs(idx+1,dimr))
        
        
        return dfs(0,0)