class Solution(object):
    def putQ(self, n, row, board, cols, posD, negD, res):
        if row == n:
            copy = [''.join(j) for j in board]
            res.append(copy)
            return
        for i in range(n):
            if i in cols or (row + i) in posD or (row - i) in negD:
                continue
            cols.add(i)
            posD.add(row + i)
            negD.add(row - i)
            board[row][i] = 'Q'
            self.putQ(n, row+1, board, cols, posD, negD, res)
            cols.remove(i)
            posD.remove(row + i)
            negD.remove(row - i)
            board[row][i] = '.'
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = set()
        posD = set()
        negD = set()
        row = 0
        res = []
        board = [['.']*n for i in range(n)]
        self.putQ(n, row, board, cols, posD, negD, res)
        return res
