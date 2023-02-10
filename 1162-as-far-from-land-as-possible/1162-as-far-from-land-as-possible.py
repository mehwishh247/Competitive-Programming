class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

            q = deque()
            seen = set()
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == 1:
                        q.append((x,y,0))

            while q:
                x, y, steps = q.popleft()
                if (x,y) in seen or not ((0 <= x < len(grid)) and (0 <= y < len(grid))):
                    continue
                seen.add((x,y))
                grid[x][y] = steps
                dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                for dx,dy in dirs:
                    q.append((x+dx, y+dy, steps+1))

            ans = max([max(v) for v in grid])
            return ans if ans != 0 else -1
