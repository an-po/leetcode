from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidSudokuXY(board, x, y):
            for k in range(9):
                if (k != x) and (board[y][k] == board[y][x]):
                    return False
                if (k != y) and (board[k][x] == board[y][x]):
                    return False
            cell_x = (x // 3) * 3
            cell_y = (y // 3) * 3
            for k in range(9):
                i = cell_x + k % 3
                j = cell_y + k // 3
                if ((i != x) or (j != y)) and (board[j][i] == board[y][x]):
                    return False
            return True

        def recursion(board, x, y):
            while (x < 9) and (y < 9) and board[y][x] != '.':
                x += 1
                if x == 9:
                    x = 0
                    y += 1
            if y == 9:
                return True
            for k in range(1, 10):
                board[y][x] = str(k)
                if isValidSudokuXY(board, x, y):
                    if recursion(board, x, y):
                        return True
            board[y][x] = '.'
            return False

        recursion(board, 0, 0)

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
s = Solution()
s.solveSudoku(board)
print(board)