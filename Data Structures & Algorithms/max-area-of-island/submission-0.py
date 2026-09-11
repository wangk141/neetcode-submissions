class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            currCount = 1
            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    if (row + dr in range(rows) and col + dc in range(cols) and (row + dr, col + dc) not in visited and grid[row + dr][col + dc] == 1):
                        q.append((row + dr, col + dc))
                        currCount += 1
                        visited.add((row + dr, col + dc))
            return currCount
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r,c), maxArea)
        return maxArea