class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-x for x in stones]
        heapq.heapify(s) # max heap

        while len(s) > 1:
            l, r = heapq.heappop(s) * -1, heapq.heappop(s) * -1
            diff = abs(l-r)
            if diff > 0:
                heapq.heappush(s, diff * -1)
        
        return s[0] * -1 if s else 0



        