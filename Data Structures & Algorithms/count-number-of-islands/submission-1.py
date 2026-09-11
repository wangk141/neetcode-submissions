class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        # visited = ()

        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        for r in range(ROWS):
            for j in range(COLS):
                if grid[r][j] == "1":
                    queue.append((r, j))
                    while queue:
                        row, col = queue.popleft()
                        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                        for dr, dc in directions:
                            if 0 <= row + dr < ROWS and 0 <= col + dc < COLS and grid[row + dr][col + dc] == "1":
                                queue.append((row + dr, col + dc))
                                grid[row + dr][col + dc] = "0"
                    count += 1
        return count
                        
            
