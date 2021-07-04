class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * (len(nums) + 1)
        return self.max_money(nums, len(nums), dp)
    
    def max_money(self, nums, n, dp):
        if n <= 0:
            return 0
        
        if dp[n] is not None:
            return dp[n]
        
        dp[n] = max(
            nums[n-1] + self.max_money(nums, n-2, dp),
            self.max_money(nums, n-1, dp)
        )
        
        return dp[n]
        