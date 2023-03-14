class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        inf = -1*float('inf')
        heights.append(inf)
        stack = []
        g_max = 0
        for idx,height in enumerate(heights):
            while stack and stack[-1][-1]>height:
                removed = stack.pop()
                left = stack[-1][0] if stack else -1
                right = idx
                # span[f'{removed[-1]}-{removed[0]}'] = [left,right]
                g_max = max(g_max, (right-left-1)*removed[-1])
            stack.append((idx,height))
        return g_max
