class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                lst.append(matrix[top][i])
            top += 1

            for j in range(top, bottom):
                lst.append(matrix[j][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for k in range(right - 1, left - 1, -1):
                lst.append(matrix[bottom - 1][k])
            bottom -= 1

            for l in range(bottom - 1, top -1 , -1):
                lst.append(matrix[l][left])
            left += 1
        return lst
