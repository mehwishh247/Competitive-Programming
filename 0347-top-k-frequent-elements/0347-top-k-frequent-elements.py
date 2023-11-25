class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count nums   1:1 2:1
        
        count = Counter(nums)  # time n and space n
        
        freq = [[] for i in range(len(nums)+1)]
        
        for key,value in count.items(): # time n and space n
            freq[value].append(key)
            
        res = [] # time and space k
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
            
        
        
        
            
        