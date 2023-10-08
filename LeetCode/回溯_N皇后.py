class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0, result)
        return result
    
    def backtrack(self, board, row, result):
        if row == len(board):
            result.append([''.join(row) for row in board])
            return
        
        for col in range(len(board[row])):
            if self.is_valid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, row + 1, result)
                board[row][col] = '.'
    
    def is_valid(self, board, row, col):
        n = len(board)
        
        # 检查列是否有皇后
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        
        # 检查左上方是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # 检查右上方是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True