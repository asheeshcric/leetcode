class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                
# Optimized solution using a dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i,num in enumerate(nums):
            if (target - num) in seen:
                return [i, seen[target-num]]
            else:
                seen[num] = i
