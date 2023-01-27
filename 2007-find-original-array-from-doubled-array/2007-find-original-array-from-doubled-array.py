class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt,ans=Counter(changed),[]
        if len(changed)%2:
            return []
        for x in sorted(cnt.keys()):
            # if the frequency of the current number is greater than the frequency of it double it can not be possible  
            if cnt[x]>cnt[x*2]:
                return []
            # if the current number is zero then it must have even number of frequency to return half of them
            if x==0:
                if cnt[x]%2:
                    return []
                else:
                    ans+=[0]*(cnt[x]//2)
            else:
                ans+=[x]*cnt[x]
            # after solving for the current number reduce the frequency of its double by the frequency of the current number
            cnt[2*x]-=cnt[x]
        return ans