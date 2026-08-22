class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:      # left wall is shorter → move it in
                l += 1
            else:                          # right wall is shorter (or equal) → move it in
                r -= 1

        return max_area