class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = min(height[i], height[-1]) * (len(height) - 1)
        while i < j:
            if height[i] < height[j]:
                while height[i] < height[j]:
                    i += 1
            else
                j -= 1

        return max_area

c = Solution()
print(c.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))