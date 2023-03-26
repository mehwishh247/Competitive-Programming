class Solution:
            
    def evenOddBit(self, n: int) -> List[int]:
        bnry = str(bin(n))[2:]
        res=[0,0]
        n=len(bnry)-1
        for i in range(n,-1,-1):
            if (n-i) %2!=0:
                res[1]+=int(bnry[i])
            elif (n-i)%2==0:
                res[0]+=int(bnry[i])
        return res
                
        
        
        
        