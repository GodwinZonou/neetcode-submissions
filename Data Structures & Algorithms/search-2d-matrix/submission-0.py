class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row_l, row_r = 0, m-1
        while row_l <= row_r:
            mid_row = row_l + ((row_r - row_l)//2)
            x, y = matrix[mid_row][0], matrix[mid_row][n-1]
            if target<x:
                row_r = mid_row-1
            elif target>y:
                row_l = mid_row+1
            else:
                break

        col_l, col_r = 0, n-1
        while col_l <= col_r:
            mid_col = col_l + ((col_r - col_l)//2)
            if target<matrix[mid_row][mid_col]:
                col_r = mid_col-1
            elif target>matrix[mid_row][mid_col]:
                col_l = mid_col+1
            else:
                return True
        return False