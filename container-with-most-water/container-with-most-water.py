class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_width = len(height) - 1
        left, right = 0, max_width
        max_area = 0
        for width in range(max_width, 0, -1):
            if height[left] < height[right]:
                max_area = max(max_area, width * height[left])
                left = left + 1

            else:
                max_area = max(max_area, width * height[right])
                right = right - 1

        return max_area
        