class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        dp = [1 for _ in range(len(nums))]
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(1 + dp[i], dp[j])

                    
        print(dp)
        return max(dp)