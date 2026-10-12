from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 boxes
        # 9 rows
        # 9 columns
        # (row: i, col: j) => square_set (i // 3) * 3 + (j // 3)

        row_sets = defaultdict(lambda: set())
        col_sets = defaultdict(lambda: set())
        square_sets = defaultdict(lambda: set())

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                if val in row_sets[row]:
                    return False
                row_sets[row].add(val)

                if val in col_sets[col]:
                    return False
                col_sets[col].add(val)

                square_ind = (row//3)*3 + (col//3)

                if val in square_sets[square_ind]:
                    return False
                square_sets[square_ind].add(val)
        
        return True
