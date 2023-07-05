class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        def generate_prime_numbers(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False

            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                p += 1

            prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
            return prime_numbers
        
        allPrimes = generate_prime_numbers(n)
        
        look = set(allPrimes)
        visited = set()
        
        ans = []
        
        for pr in allPrimes:   
            if pr not in visited and n-pr in look:
                ans.append([pr,n-pr])
                visited.add(pr)
                visited.add(n-pr)
        return ans

        
        
    