class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(Counter(nums), key=Counter(nums).get, reverse=True)[:k]
        