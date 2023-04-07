class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        lg = len(piles)//3
        piles.sort()
        ans=0
        for i in range(lg,len(piles),2):
            ans+=piles[i]
        return ans
        '''
[2,3,3,3,4,5,6,7,7,8,10,12]
 0 1 2 3 4 5 6 7 8 9 10 11

12//3-1=3
[3,10,12]
[3,7,8]
[3,6,7]
[2,4,5]

27

'''