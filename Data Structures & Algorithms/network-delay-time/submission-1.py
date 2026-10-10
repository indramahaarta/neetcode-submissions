class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for t in times:
            u, v, w = t
            adj[u].append((w, u, v))
        
        visited = set()
        queue = adj[k] 
        heapq.heapify(queue)
        visited.add(k)
        maxW = -float('inf')

        while len(visited) < n and queue:
            w, u, v = heapq.heappop(queue)
            if v in visited: continue
            visited.add(v)
            maxW = max(maxW, w)

            for nw, nu, nv in adj[v]:
                if nv in visited: continue
                heapq.heappush(queue, (nw + w, nu, nv))
        
        if len(visited) < n:
            return -1
        
        return maxW


        