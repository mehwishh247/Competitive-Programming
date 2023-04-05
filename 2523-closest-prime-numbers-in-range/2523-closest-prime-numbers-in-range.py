class Solution:
    def is_prime(self,num):
            if num==1:
                return False
            used = 2
            cap=int(num**0.5)+1
            for i in range(2,cap):
                if num%i==0:
                    used+=1
                if used>2:
                    return False
            return True
    def closestPrimes(self, a: int, b: int) -> List[int]:
            i,j=a,a+1
            lib = defaultdict(list)
            mnn=float('inf')
            while j<=b:
                if self.is_prime(i):
                    if self.is_prime(j):
                        temp = [i,j]
                        if j-i<=2:
                            return temp
                        lib[j-i].append(temp)
                        mnn=min(mnn,j-i)
                        i=j
                        j+=1
                    else:
                        j+=1
                else:
                    i+=1
                    j+=1
            if lib[mnn]:
                return lib[mnn][0]
            return [-1,-1]