class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        for i in range(len(nums)):
            nums[i] = nums[i] + i
        
        i = 0
        ans = 1
        while nums[i] < len(nums) - 1:
            js, je = i + 1, nums[i]

            while js < je + 1:
                if nums[js] >= len(nums) - 1:
                    return ans + 1

                if nums[js] > nums[i]:
                    i = js
                
                js += 1

            ans += 1
        
        return ans



        