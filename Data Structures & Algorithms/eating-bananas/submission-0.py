class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for i in piles:
            max_val = max(max_val, i)
        
        l, r = 1, max_val
        while l < r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                r = mid
            elif time > h:
                l = mid + 1

        return r


        