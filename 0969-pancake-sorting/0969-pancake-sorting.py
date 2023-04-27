class Solution:
    
    def maxIdx(self,arr,x):
        minn = max(arr[:x])
        for i in range(x):
            if arr[i]==minn:
                return i
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ref = sorted(arr)
        ans = []
        n=len(arr)
        
        while n:
            
            revIdx = self.maxIdx(arr,n)

            front = arr[:revIdx+1][::-1]
            remain = arr[revIdx+1:]
            front.extend(remain)
            
            ans.append(revIdx+1)
            ans.append(n)
            
            frt = front[:n][::-1]
            rem = front[n:]
            
            frt.extend(rem)

            arr = frt
            n-=1
            
        
        
        return ans