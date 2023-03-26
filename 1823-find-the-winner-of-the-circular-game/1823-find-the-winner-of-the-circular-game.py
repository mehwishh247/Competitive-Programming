class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    
            arr = [x for x in range(1,n+1)]
            cap = n
            c=k-1
            p=0
            while cap>1:
                if p==c and arr[p]!=0:
                    arr[p]=0
                    c=(c+k)%n
                    # p=p+1
                    cap-=1 
                p=(p+1)%n
                if arr[p]==0:
                    c= (c+1)%n

            arr.sort()
            return arr[-1]
