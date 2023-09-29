class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
    
        text1 = s   
        text2 = s[::-1]
        
        n=m = len(s)
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[n][m] 