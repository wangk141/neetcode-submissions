class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         visited = set()

#         ROWS, COLS = len(board), len(board[0])

#         def dfs(r, c, reachEdge):
#             directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
#             visited.add((r, c))
#             if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
#                 reachEdge = True
#             for dr, dc in directions:
#                 dfs(r + dr, c + dc, visited, reachEdge)
#             if reachEdge == True:
#                 board[r][c] = 'X'  

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if min(r, c) < 0 or r > ROWS or c >= COLS or board[r][c] == 'X' or (r, c) in visited:
#                     return
#                 if board[r][c] == 'O':
#                     dfs(r, c, False)
