class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp = math.gcd(temp, nums[j])
                if temp == k:
                    ans += 1
                elif temp < k:
                    break
        return ans
#         i=j=0
#         ans=0
#         # pos = defaultdict(list)
#         pos = defaultdict(int)

#         while j<len(nums):
#             if nums[j]==k:
#                 # pos[nums[i]].append(nums[j])
#                 pos[nums[i]]+=1
#                 j+=1
#             elif nums[j]%k==0:
#                 # pos[nums[i]].append(nums[j])
#                 pos[nums[i]]+=1
#                 j+=1
#             else:
#                 i=j+1
#                 j=i
#         print(pos,ans)
#         for key in pos:
#             if pos[key]==k:
#                 ans+=1
#             elif pos[key]>2:
#                 pp = (pos[key])(pos[key]-1)//2
#                 ans+=pp
#         return ans
