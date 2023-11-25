class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = len(strs)
        all_counts = defaultdict(list) #n
        
        for i in range(n):
            
            count = [0]*26
            
            for c in strs[i]:    
                count[ord(c)-ord("a")]+=1
            
            all_counts[tuple(count)].append(strs[i])
            
            
        return all_counts.values()
            
        