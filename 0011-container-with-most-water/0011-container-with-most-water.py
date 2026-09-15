class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0

        l = 0
        r = len(height) - 1

        while l < r:
            wid = r - l
            hei = min(height[l], height[r])

            ar = wid * hei
            mx = max(mx, ar)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mx