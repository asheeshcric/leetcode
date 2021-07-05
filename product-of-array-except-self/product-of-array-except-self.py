class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        for num in nums:
            output.append(prod)
            prod *= num
            
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
            
        return output