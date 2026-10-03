class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}
        for edge in edges:
            x, y = edge[0], edge[1]

            if x not in d: d[x] = []
            if y not in d: d[y] = []

            d[x].append(y)
            d[y].append(x)
        
        visited = set()
        def bfs(x):
            q = deque([x])

            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    visited.add(i)
                    
                    if i not in d:
                        return

                    for j in d[i]:
                        if j not in visited:
                            q.append(j)
        
        ctr = 0
        for i in range(n):
            if i in visited:
                continue
            
            bfs(i)
            ctr += 1

        return ctr
            

            

        