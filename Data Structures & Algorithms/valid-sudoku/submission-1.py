class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # we need a default dict which will be mapped to a set()
        # which will be used to store the elements in a specific row
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        print(rows)
        print(squares)
        return True
