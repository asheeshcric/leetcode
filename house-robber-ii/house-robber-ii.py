class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return 0
        
        dp1 = [None] * len(nums)
        dp2 = [None] * len(nums)
        ans = max(
            self.max_money(nums[1:], len(nums) - 1, dp1), self.max_money(nums[:-1], len(nums) - 1, dp2)
        )
        return ans
    
    def max_money(self, nums, n, dp):
        if n <= 0:
            return 0

        if dp[n] is not None:
            return dp[n]

        dp[n] = max(nums[n - 1] + self.max_money(nums, n - 2, dp), self.max_money(nums, n - 1, dp))
        return dp[n]