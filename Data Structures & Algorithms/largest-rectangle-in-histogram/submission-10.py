class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 

        for i, h in enumerate(heights):
            start = i
            
            while stack and heights[stack[-1]] > h:
                start = stack.pop()
                peak = heights[start]
                res = max(res, peak * (i - start))
            
            heights[start] = h
            stack.append(start)

        end = len(heights)

        for start in stack:
            res = max(res, heights[start] * (end - start))

        return res