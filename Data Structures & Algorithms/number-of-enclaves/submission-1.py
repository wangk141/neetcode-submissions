class Solution:
    from collections import deque
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        visited = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1) and grid[i][j] == 1:
                    visited.append((i, j))
        
        while visited:
            r, c = visited.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] == 1:
                    visited.append((r + dr, c + dc))
            grid[r][c] = 0
        counter = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    counter += 1
        return counter