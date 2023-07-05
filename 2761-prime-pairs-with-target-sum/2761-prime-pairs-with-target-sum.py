class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        def generate_prime_numbers(n):
            primes = [1] * (n + 1)
            primes[0] = primes[1] = 0

            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = 0
                p += 1

            prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
            return prime_numbers
        
        allPrimes = generate_prime_numbers(n)
        
        look = set(allPrimes)        
        ans = []
        
        for pr in allPrimes:  
            
            if pr<=n-pr and n-pr in look:
                ans.append([pr,n-pr])

        return ans
    
