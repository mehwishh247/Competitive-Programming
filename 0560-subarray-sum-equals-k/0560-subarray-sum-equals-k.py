class Solution:
    def subarraySum(self, arr: List[int], target: int) -> int:
        pre_sum = []
        pre_sum.append(arr[0])
        for i in range(1,len(arr)):
            pre_sum.append(pre_sum[-1]+arr[i])
        viewed = defaultdict(int)
        viewed[0]=1
        count = 0
        for i in range(len(pre_sum)):
            if viewed[pre_sum[i]-target]:
                count+=viewed[pre_sum[i]-target]
            viewed[pre_sum[i]]+=1

        return count    
        