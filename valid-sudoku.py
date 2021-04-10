class Solution(object):
    def isValidSudoku(self, board):

        if not board or len(board) == 0:
            return False

        def check_rows(board):
            for i in range(0, 9):
                hset = set()
                for j in range(0, 9):
                    if board[i][j] != '.':
                        num = int(board[i][j])
                        if num in hset:
                            return False
                        else:
                            hset.add(num)
            return True

        def check_columns(board):
            for j in range(0, 9):
                hset = set()
                for i in range(0, 9):
                    if board[i][j] != '.':
                        num = int(board[i][j])
                        if num in hset:
                            return False
                        else:
                            hset.add(num)
            return True

        def check_squares(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    hset = set()
                    for m in range(i, i+3):
                        for n in range(j, j+3):
                            if board[m][n] != '.':
                                num = int(board[m][n])
                                if num in hset:
                                    return False
                                hset.add(num)

            return True

        if not check_rows(board):
            return False
        if not check_columns(board):
            return False
        if not check_squares(board):
            return False

        return True
