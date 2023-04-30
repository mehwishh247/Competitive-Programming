class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        # Enqueue all cells with value 0 and set cells with value 1 to a large value
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float('inf')
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS to update cells with value 1
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    dist = mat[row][col] + 1
                    if dist < mat[new_row][new_col]:
                        mat[new_row][new_col] = dist
                        queue.append((new_row, new_col))

        return mat