class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bit_masks = [0] * n
        for i in range(n):
            for c in words[i]:
                bit_masks[i] |= 1 << (ord(c) - ord('a'))
        
        maxx = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if bit_masks[i] & bit_masks[j] == 0:
                    posAns = len(words[i]) * len(words[j])
                    maxx = max(maxx, posAns)
        
        return maxx