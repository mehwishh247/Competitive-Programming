class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        heapify(stones)
        
        while len(stones)>=2:
            temp=[]
            while len(stones)>2:
                temp.append(heappop(stones))
            large,largest=heappop(stones),heappop(stones)
            
            if largest-large:
                temp.append(largest-large)
            for val in temp:
                heappush(stones,val)
        
        if len(stones):
            return stones[0]
        return 0