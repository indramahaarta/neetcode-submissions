class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = [float('inf')]*(len(cost)+1)
        stairs[0], stairs[1] = 0, 0
        for i in range(2, len(stairs)):
            stairs[i] = min(stairs[i-1] + cost[i-1], stairs[i-2] + cost[i-2])
        
        return stairs[-1]

        