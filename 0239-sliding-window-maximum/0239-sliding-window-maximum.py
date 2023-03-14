class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        for i in range(k):
            while que and que[-1][-1]<nums[i]:
                que.pop()
            que.append((i,nums[i]))

        result = []
        result.append(que[0][-1])

        for i in range(k,len(nums)):
            while que and que[-1][-1]<nums[i]:
                que.pop()
            que.append((i,nums[i]))

            firstEleIdx = que[0][0]
            if firstEleIdx<i-k+1:
                que.popleft()  
            result.append(que[0][-1])

        return result
        