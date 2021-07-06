class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            current_length = 1
            if num - 1 not in nums:
                # num is the start of a sequence
                while num + 1 in nums:
                    current_length += 1
                    num = num + 1
                max_length = max(max_length, current_length)

        return max_length