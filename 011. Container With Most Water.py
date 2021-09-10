class Solution:
    def maxArea(self, height):
        max_v = 0
        start = 0
        stop = len(height)-1
        while start < stop:
            v = min(height[start], height[stop]) * (stop - start)
            if v > max_v:
                max_v = v
            if height[start] > height[stop]:
                stop -= 1
            else:
                start += 1
        return int(max_v)