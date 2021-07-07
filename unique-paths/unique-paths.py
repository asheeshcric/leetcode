class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[None for c in range(n+1)] for r in range(m+1)]
        return self.find_paths(m, n, row=0, col=0)
    
    def find_paths(self, m, n, row, col):
        if row == m-1 and col == n-1:
            return 1
        
        if row < 0 or row >= m or col < 0 or col >= n:
            return 0
        
        if self.dp[row][col] is not None:
            return self.dp[row][col]
        
        self.dp[row][col] = self.find_paths(m, n, row, col+1) + self.find_paths(m, n, row+1, col)
        return self.dp[row][col]