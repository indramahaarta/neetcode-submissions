class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            target = -val

            if i > 0 and val == nums[i-1]:
                continue

            l, h = i+1, len(nums)-1
            while l < h:
                if nums[l] + nums[h] > target:
                    h -= 1
                elif nums[l] + nums[h] < target:
                    l += 1
                else:
                    if res:
                        if res[-1] != [val, nums[l], nums[h]]:
                            res.append([val, nums[l], nums[h]]) 
                    else:
                        res.append([val, nums[l], nums[h]]) 
                    
                    cur_h = nums[h]
                    while h > 0 and nums[h] == cur_h:
                        h -= 1
                    
                    cur_l = nums[l]
                    while l < len(nums) and nums[l] == cur_l:
                        l += 1
                    
                    
        return res

        