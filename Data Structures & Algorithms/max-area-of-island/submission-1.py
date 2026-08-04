class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()
        l_r = len(grid)
        l_c = len(grid[0])
        
        def bfs(r, c) -> int:
            # print("bfs called")
            queue = collections.deque([(r,c)])
            seen.add((r,c))
            total = 0

            while queue:
                cur_r, cur_c = queue.popleft()
                total += 1

                direction = [[1,0], [-1,0], [0,1], [0,-1]]
                for a_r, a_c in direction:
                    temp_r, temp_c = cur_r + a_r, cur_c + a_c

                    if temp_r in range(l_r) and temp_c in range(l_c) and grid[temp_r][temp_c] == 1 and (temp_r, temp_c) not in seen:
                        seen.add((temp_r, temp_c))
                        queue.append((temp_r, temp_c))
            # print(seen, total)
            return total
        
        res = 0
        for r in range(l_r):
            for c in range(l_c):
                if grid[r][c] == 1 and (r,c) not in seen:
                    res = max(res, bfs(r, c))
        
        return res


