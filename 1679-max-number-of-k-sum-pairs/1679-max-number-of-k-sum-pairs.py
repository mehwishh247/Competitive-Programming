class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        c = 0
        for i in nums:   
            if k-i != i:
                if cnt[k-i]>=1 and cnt[i]>=1:
                    cnt[i]-=1
                    cnt[k-i]-=1
                    c+=1
            else:
                if cnt[i]>=2:
                    cnt[i]-=2
                    c+=1


        return c
