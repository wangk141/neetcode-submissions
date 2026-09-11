class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def bfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist += 1


        # FAILED ATTEMPT
        # rows, cols = len(grid), len(grid[0])

        # def bfs(i, j):
        #     q = collections.deque();
        #     q.append((i, j))
        #     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        #     visited = set()
        #     count = 0
        #     while q:
        #         for dr, dc in directions:
        #             i, j = q.popleft()
        #             r, c = i + dr, j + dc
        #             if (r in range(rows) and c in range(cols) and (r,c) not in visited):
        #                 if grid[r][c] == 0:
        #                     return count + 1
        #                 elif grid[r][c] == -1:
        #                     pass
        #                 else:
        #                     q.append((r, c))
        #                     count += 1
        #                     visited.add((r,c))

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == -1 or grid[i][j] == 0:
        #             pass
        #         else:
        #             grid[i][j] = bfs(i, j)
        

                    
