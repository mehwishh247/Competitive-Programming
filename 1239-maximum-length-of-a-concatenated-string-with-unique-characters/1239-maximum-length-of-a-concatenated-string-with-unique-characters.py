class Solution: 
    def maxLength(self, arr: List[str]) -> int:
        
        ans=0
        total_set = set()
        n =len(arr)
        def recSol(idx):
            nonlocal ans
            ans = max(ans,len(total_set))   
            for i in range(idx,n):
                     now = set(list(arr[i]))
                     if len(now)==len(arr[i]) and not total_set.intersection(now):
                            for j in arr[i]: total_set.add(j)
                            recSol(i+1)
                            for j in arr[i]: total_set.discard(j)

        recSol(0)
        return ans
