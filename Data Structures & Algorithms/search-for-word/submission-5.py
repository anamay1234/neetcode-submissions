class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # stores coordinates we have already gone to
        path = set()

        def dfs(i, j, k):
            if k >= len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in path:
                return False

            if board[i][j] == word[k]:
                path.add((i, j))
                if dfs(i+1, j, k+1): 
                    return True
                if dfs(i-1, j, k+1):
                    return True
                if dfs(i, j+1, k+1):
                    return True
                if dfs(i, j-1, k+1):
                    return True

                path.remove((i, j))
            else:
                
                return False   


        for i in range(len(board)):
            for j in range(len(board[0])):
                path.clear()
                res = dfs(i, j, 0)
                if res:
                    return True
        
        return False

        


        