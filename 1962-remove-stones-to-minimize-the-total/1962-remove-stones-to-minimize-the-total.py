class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        minHeap = [-x for x in piles]
        
        heapify(minHeap)
        
        for i in range(k):
            
            x = -heappop(minHeap)
            x-=x//2
            heappush(minHeap,-x)
        
        return -sum(minHeap)