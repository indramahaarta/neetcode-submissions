from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotten = 2

        q = deque()
        visited = set()
        fresh_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == rotten:
                    q.append((row, col))
                elif grid[row][col] == fresh:
                    fresh_count += 1
        
        def addCell(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != fresh:
                return
            
            q.append((row, col))

        time = 0
        while q:
            fresh_toggle = False
            for _ in range(len(q)):
                row, col = q.popleft()
                if (row, col) in visited:
                    continue
                
                if grid[row][col] == fresh:
                    fresh_count -= 1
                    fresh_toggle = True
                
                grid[row][col] = rotten
                visited.add((row, col))

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for r, c in directions:
                    addCell(row + r, col + c)
            
            if fresh_toggle:
                time += 1
        
        return time if fresh_count == 0 else -1


        