class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c) -> None:
            grid[r][c] = "0"
            if r + 1 < len(grid) and grid[r+1][c] == "1":
                bfs(r+1, c)
            
            if c + 1 < len(grid[0]) and grid[r][c+1] == "1":
                bfs(r, c+1)
            
            if r - 1 >= 0 and grid[r-1][c] == "1":
                bfs(r-1, c)
            
            if c - 1 >= 0 and grid[r][c-1] == "1":
                bfs(r, c-1)



        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "0":
                    continue
                
                count += 1
                bfs(r, c)
        
        return count
                


        