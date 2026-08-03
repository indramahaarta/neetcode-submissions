class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        p = [(math.sqrt(x**2 + y**2), x, y) for x, y in points]

        heapq.heapify(p)
        res = []
        while len(res) < k and p:
            el = heapq.heappop(p)
            res.append([el[1], el[2]])

        return res
        