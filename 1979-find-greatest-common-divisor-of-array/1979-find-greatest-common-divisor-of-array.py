class Solution:
    
    
    def primeFactor(self,num):
        used = defaultdict(int)
        cap=int(num**0.5)+1
        for i in range(2,cap):
            while num>1 and num%i==0:
                num=num//i
                used[i]+=1
        if num>1:
            used[num]+=1
        return used
   
    def findGCD(self, nums: List[int]) -> int:
        x,y= min(nums),max(nums)
    
        primeX = self.primeFactor(x)
        primeY = self.primeFactor(y)
        ans=1
        for key in primeX.keys():
            if primeY[key]>=1:
                ans*= key**min(primeX[key],primeY[key])

        return ans