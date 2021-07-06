class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums = sorted(nums)
        triplets = set()
        for i in range(0, n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    triplets.add(triplet)
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
                    
        return [list(triplet) for triplet in triplets]