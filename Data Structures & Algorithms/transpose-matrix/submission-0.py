class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # issue is lists are mutable
        
        ROWS, COLS = len(matrix), len(matrix[0])

        res = [[0] * ROWS for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                res[j][i] = matrix[i][j]
        
        return res