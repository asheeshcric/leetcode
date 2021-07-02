class Solution:
    
    def climbStairs(self, n: int) -> int:
        self.dp = [None for _ in range(n+1)]
        return self.check_steps(n)
        
    def check_steps(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if self.dp[n] is not None:
            return self.dp[n]
        
        self.dp[n] = self.check_steps(n-1) + self.check_steps(n-2)
        return self.dp[n]