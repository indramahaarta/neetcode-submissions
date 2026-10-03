class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {}
        for edge in edges:
            x, y = edge[0], edge[1]

            if x not in d: d[x] = []
            if y not in d: d[y] = []

            d[x].append(y)
            d[y].append(x)
        
        start, prev, visited = 0, -1, set()

        def dfs(start, prev):
            visited.add(start)

            if start not in d:
                return True

            for i in d[start]:
                if i == prev:
                    continue
                if i in visited:
                    return False

                if not dfs(i, start):
                    return False
            
            return True
        
        return dfs(start, prev) and len(visited) == n

        