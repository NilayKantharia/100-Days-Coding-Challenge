class Solution(object):
    def dfs(self, r, c, i, board, word):
        if i == len(word) : return True
        if (r < 0 or c < 0 or r >= self.ROW or c >= self.COL or (r,c) in self.path or word[i] != board[r][c]):
            return False
        
        self.path.add((r,c))
        res = (self.dfs(r + 1, c, i + 1, board, word) or
                self.dfs(r - 1, c, i + 1, board, word) or 
                self.dfs(r, c + 1, i + 1, board, word) or
                self.dfs(r, c - 1, i + 1, board, word)
            )
        self.path.remove((r,c))
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0 : return True
        self.ROW = len(board)
        self.COL = len(board[0])
        self.path = set()
        
        for r in range(self.ROW):
            for c in range(self.COL):
                if self.dfs(r, c, 0, board, word) : return True
        return False
        
