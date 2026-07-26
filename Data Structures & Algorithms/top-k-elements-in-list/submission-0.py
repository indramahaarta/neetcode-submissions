from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        l = []
        for key, val in d.items():
            l.append((-val, key))
        
        heapq.heapify(l)

        i = 0
        res = []
        while i < k:
            val, key = heapq.heappop(l)
            res.append(key)
            i += 1
        
        return res

        


        