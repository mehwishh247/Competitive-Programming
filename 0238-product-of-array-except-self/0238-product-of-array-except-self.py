class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        pre.append(nums[0])

        for i in range(1,len(nums)):
            pre.append(pre[-1]*nums[i])

        post=[1]*len(nums)
        post[-1]=nums[-1]
        for j in range(len(nums)-2,-1,-1):
            post[j]=nums[j]*post[j+1]
            
        res=[]
        res.append(post[1])

        for x in range(1,len(nums)-1):
            res.append(pre[x-1]*post[x+1])
        res.append(pre[-2])
        
        return res
