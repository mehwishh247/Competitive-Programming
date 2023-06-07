class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def isValid(i: int, j: int, n: int) -> bool:
            return (i >= 0 and i < n and j >= 0 and j < n)

        def dfs(i: int, j: int, n: int, grid: List[List[int]]) -> None:
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return

            grid[i][j] = -1

            dfs(i - 1, j, n, grid)
            dfs(i + 1, j, n, grid)
            dfs(i, j - 1, n, grid)
            dfs(i, j + 1, n, grid)

        n = len(grid)

        # Step 1: Find the first island using DFS and mark its cells as -1
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j, n, grid)
                    found = True
                    break

        # Step 2: Perform a BFS search to find the second island
        q = deque()
        steps = 0

        # Add the cells of the first island to the BFS queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    q.append((i, j))

        # Perform BFS search
        while q:
            size = len(q)

            while size > 0:
                node = q.popleft()

                for x in range(4):
                    ni = node[0] + dx[x]
                    nj = node[1] + dy[x]

                    if isValid(ni, nj, n):
                        if grid[ni][nj] == 1:
                            return steps

                        if grid[ni][nj] == 0:
                            grid[ni][nj] = -1
                            q.append((ni, nj))

                size -= 1

            steps += 1

        return -1 # No path found