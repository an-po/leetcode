from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            raw_set = set()
            col_set = set()
            cell_set = set()
            for j in range(9):
                if board[i][j] != '.' and (board[i][j] in raw_set):
                    return False
                else:
                    raw_set.add(board[i][j])
                if board[j][i] != '.' and (board[j][i] in col_set):
                    return False
                else:
                    col_set.add(board[j][i])
                y = (i // 3) * 3 + j // 3
                x = (i % 3) * 3 + j % 3
                if board[y][x] != '.' and (board[y][x] in cell_set):
                    return False
                else:
                    cell_set.add(board[y][x])
        return True



s = Solution()
board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))
