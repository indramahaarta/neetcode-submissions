class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        curMax = nums[0]

        for i in range(1, len(nums)):
            curMax = nums[i] if curMax + nums[i] < nums[i] else curMax + nums[i]

            if curMax > mx:
                mx = curMax
            
            # print(curMax, mx)
        
        return mx
        