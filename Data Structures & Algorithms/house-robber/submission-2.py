class Solution:
    def rob(self, nums: List[int]) -> int:
        mx = [0]*len(nums)
        mx[0] = nums[0]
        if len(nums) > 1:
            mx[1] = max(mx[0], nums[1])

        for i in range(2, len(nums)):
            mx[i] = max(mx[i-1], mx[i-2] + nums[i])
        
        return mx[-1]
        