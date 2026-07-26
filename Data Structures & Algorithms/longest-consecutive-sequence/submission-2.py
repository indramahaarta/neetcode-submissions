class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mn = float("inf")
        s = set()
        for i in nums:
            s.add(i)
            mn = min(mn, i)
            
        first = []
        for i in s:
            if i-1 not in s:
                first.append(i)
        
        # print(first)
        mx = 0
        for i in first:
            cur_mx = 1
            cur_i = i
            while cur_i + 1 in s:
                cur_mx += 1
                cur_i += 1
            
            # print(i, cur_mx, s)
            mx = max(mx, cur_mx)

        return mx
            
        