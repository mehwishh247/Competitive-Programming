class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1*float('inf'))
        stack = []
        g_max = 0
        for idx,height in enumerate(heights):
            while stack and stack[-1][-1]>height:
                removed = stack.pop()
                left = stack[-1][0] if stack else -1
                g_max = max(g_max, (idx-left-1)*removed[-1])
            stack.append((idx,height))
        return g_max
