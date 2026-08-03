class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = [-n for n in nums]
        heapq.heapify(nums2)

        i = 0
        res = 0
        while i < k:
            res = -heapq.heappop(nums2)
            i += 1
        
        return res
        