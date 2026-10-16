class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = nums[:k-1]
        d = defaultdict(int)
        for i in range(len(q)):
            d[q[i]] += 1
            q[i] = -q[i]
        heapq.heapify(q)

        ans = []
        
        for i in range(k-1, len(nums)):
            heapq.heappush(q, -nums[i])
            d[nums[i]] += 1

            mx = -q[0]
            ans.append(mx)

            d[nums[i-k+1]] -= 1

            while q and d[-q[0]] <= 0:
                x = heapq.heappop(q)

        
        return ans


        