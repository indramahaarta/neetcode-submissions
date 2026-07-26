from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = [[] for i in range(len(nums) + 1)]
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
        
        for key, val in d.items():
            l[val].append(key)
        
        i = n
        res = []
        for i in range(len(l)-1,0,-1):
            res.extend(l[i])

        return res[:k]


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

        


        