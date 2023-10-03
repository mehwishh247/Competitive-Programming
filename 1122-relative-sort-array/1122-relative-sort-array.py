class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        cnt = Counter(arr1)
        
        result = []
        for num in arr2:
            result += [num] * cnt[num]
            cnt[num]=0
        arr = sorted(cnt.keys())
        for num in arr:
            result += [num] * cnt[num]
        return result