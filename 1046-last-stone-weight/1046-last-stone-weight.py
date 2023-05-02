class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while len(stones)!=1:
            rank1,rank2 = stones[-1],stones[-2]
            stones[-1]=rank1-rank2
            del stones[-2]

            stones.sort()
            
            
        return stones[0]
