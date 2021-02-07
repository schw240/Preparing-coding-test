class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        height_set = list(set(height))
        height_set.sort()

        start = 0
        end = len(height)-1
        for i in range(len(height_set)):
            for k in range(start, len(height)):
                if height[k] >= height_set[i]:
                    start = k
                    break
            for k in range(end, -1, -1):
                if height[k] >= height_set[i]:
                    end = k
                    break

            x = end-start
            y = height_set[i]
            maxarea = max(maxarea, x*y)

        return maxarea
