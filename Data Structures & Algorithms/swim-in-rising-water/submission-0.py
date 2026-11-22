class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q, visited = [], set()
        q.append([grid[0][0], 0, 0])

        while q:
            w, i, j = heapq.heappop(q)
            if i == len(grid)-1 and j == len(grid[0]) - 1:
                return w

            if (i, j) in visited:
                continue
            visited.add((i, j))

            direction = [(0,1), (0,-1), (1, 0), (-1,0)]
            for d in direction:
                ni, nj = i + d[0], j + d[1]
                if ni >= len(grid) or ni < 0 or nj >= len(grid[0]) or nj < 0:
                    continue
                
                heapq.heappush(q, [max(w, grid[ni][nj]), ni, nj])
        
        return -1
                


        