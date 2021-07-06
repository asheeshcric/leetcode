class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        if n == 1:
            return nums[0]
        
        left, right = 0, n - 1
        while left < right:
            midpoint = int(left + (right - left)/ 2)
            if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
                return nums[midpoint]
            elif nums[left] <= nums[midpoint] and nums[right] <= nums[midpoint]:
                # This means the left half is properly sorted, so we focus on the right half
                left = midpoint + 1
            else:
                # This means the right half is properly sorted, so we focus on the left half
                right = midpoint - 1
        
        print(left)
        return nums[left]