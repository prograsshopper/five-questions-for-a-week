class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        # row
        for row in board:
            cur_row = defaultdict(lambda: 0)
            for elem in row:
                cur_row[elem] += 1
                if cur_row[elem] > 1 and elem != ".":
                    return False
        # col
        for i in range(0, len(board[0])):
            cur_col = defaultdict(lambda:0)
            for row in board:
                cur_col[row[i]] += 1
                if cur_col[row[i]] > 1 and row[i] != ".":
                    return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                subbox = defaultdict(lambda:0)
                for k in range(0, 3):
                    for l in range(0, 3):
                        subbox[board[i+k][j+l]] += 1
                        if subbox[board[i+k][j+l]] > 1 and board[i+k][j+l] != ".":
                            return False
        return True
