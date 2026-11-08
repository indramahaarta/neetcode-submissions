class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        mx = 1
        
        for i in range(1, len(nums)):
            # if nums[i] > nums[i-1]:
            #     res[i] = res[i-1] + 1
            # else:
            for j in range(i):
                if nums[j] < nums[i]:
                    res[i] = max(res[i], 1 + res[j])
            
            mx = max(mx, res[i])
        # print(res)
        return mx
        