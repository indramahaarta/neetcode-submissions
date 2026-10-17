class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # First Solution
        # q = nums[:k-1]
        # d = defaultdict(int)
        # for i in range(len(q)):
        #     d[q[i]] += 1
        #     q[i] = -q[i]
        # heapq.heapify(q)

        # ans = []
        
        # for i in range(k-1, len(nums)):
        #     heapq.heappush(q, -nums[i])
        #     d[nums[i]] += 1

        #     mx = -q[0]
        #     ans.append(mx)

        #     d[nums[i-k+1]] -= 1

        #     while q and d[-q[0]] <= 0:
        #         x = heapq.heappop(q)

        
        # return ans

        output = []
        q = deque([])
        for r in range(k-1):
            if not q:
                q.append(r)
                continue
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

        # print(q)
        
        for r in range(k-1, len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            while q[0] < r - k + 1:
                q.popleft()
            
            # print(q)
            
            output.append(nums[q[0]])

        return output

        