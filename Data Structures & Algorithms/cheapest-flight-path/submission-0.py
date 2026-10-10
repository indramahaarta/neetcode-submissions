class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        costs = [float('inf')]*n
        costs[src] = 0
        
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        for i in range(k+1):
            temp_costs = list(costs)
            for j in range(len(costs)):
                if costs[j] == float('inf'):
                    continue
                
                for v, w in adj[j]:
                    temp_costs[v] = min(temp_costs[v], costs[j] + w)
        
            costs = temp_costs
        
        return costs[dst] if costs[dst] != float('inf') else -1



        