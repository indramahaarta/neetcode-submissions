class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, ptr):
            # print(i, j)
            if ptr == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
                
            if (i, j) in visited:
                return False
            
            if word[ptr] != board[i][j]: 
                return False
            
            visited.add((i, j))
            
            directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in directions:
                if dfs(x, y, ptr+1):
                    return True
            
            visited.remove((i, j))
            
            return False
                


        for i in range(len(board)):
            for j in range(len(board[i])): 
                # print(visited)
                if dfs(i, j, 0):
                    return True
                # print(visited)
                # print("-----")
                visited.clear()

        return False
                
        