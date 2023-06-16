class Solution:

    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0], isPrime[1] = False, False
        for i in range(2, int(math.sqrt(n))+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        count = sum(1 for i in range(n) if isPrime[i])
        return count