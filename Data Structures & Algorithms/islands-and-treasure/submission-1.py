from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water = -1
        treasure_chest = 0
        land = 2147483647
        visited = set()

        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == treasure_chest:
                    q.append((row, col))
        
        def addNeighbor(row, col):
            if row == len(grid) or row < 0 or col == len(grid[0]) or col < 0 or grid[row][col] != land:
                return
            
            q.append((row, col))

        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if (row, col) in visited:
                    continue

                grid[row][col] = dist
                visited.add((row, col))
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for d_r, d_c in directions:
                    addNeighbor(row + d_r, col + d_c)
            
            dist += 1




        