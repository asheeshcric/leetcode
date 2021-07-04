class Solution:
    
    def LCS(self, text1, text2, m, n):
        if m <= 0 or n <= 0:
            return 0
        
        if self.dp[m][n] is not None:
            return self.dp[m][n]
        
        if text1[m-1] == text2[n-1]:
            self.dp[m][n] = 1 + self.LCS(text1, text2, m-1, n-1)
        else:
            self.dp[m][n] = max(
                self.LCS(text1, text2, m-1, n),
                self.LCS(text1, text2, m, n-1)
            )
            
        return self.dp[m][n]
        
        
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        self.dp = [[None for i in range(n+1)] for j in range(m+1)]
        return self.LCS(text1, text2, m, n)