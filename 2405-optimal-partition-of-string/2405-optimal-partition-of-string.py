class Solution:
    def partitionString(self, s: str) -> int:
        
        store = defaultdict(int)
        ans = 1
        
        n = len(s)
        
        for i in range(n):

            if store[s[i]]>0:
                store=defaultdict(int)
                ans+=1
            
            store[s[i]]+=1

        
        return ans
        