class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = nums[0], nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            temp = current_max * nums[i]
            current_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_min = min(nums[i], temp, nums[i] * current_min)
            max_prod = max(max_prod, current_min, current_max)

        return max_prod
        