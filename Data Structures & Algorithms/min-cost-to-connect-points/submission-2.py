class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                n1, n2 = points[i], points[j]
                adj[i].append((abs(n1[0] - n2[0]) + (abs(n1[1] - n2[1])), j))
                adj[j].append((abs(n1[0] - n2[0]) + (abs(n1[1] - n2[1])), i))
        # print(adj)
        visited = set()
        hq = []
        min_cost = 0
        for w, nei in adj[0]:
            heapq.heappush(hq, (w, 0, nei))
        visited.add(0)
        mst = []
        while len(visited) < len(points) and len(hq) > 0:
            w, start, end = heapq.heappop(hq)
            if end in visited:
                continue
            mst.append((start, end))
            visited.add(end)
            min_cost += w
            
            for next_w, next_nei in adj[end]:
                if next_nei in visited:
                    continue

                heapq.heappush(hq, (next_w, end, next_nei))

        print(mst)
        return min_cost
            

            

            

            
        