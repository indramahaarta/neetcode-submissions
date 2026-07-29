class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        cur_max = 0
        while l < r:
            cur_max = max(cur_max, (r-l)*min(heights[r], heights[l]))

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return cur_max


        