class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        def helper(arr, cur):
            if cur > len(nums) - 1:
                res.append(arr[:])
                return
            
            val = nums[cur]

            # take
            arr.append(val)
            helper(arr, cur + 1)
            arr.pop()

            # skip
            while cur < len(nums) and nums[cur] == val:
                cur += 1
            
            helper(arr, cur)
        
        helper([], 0)
        return res


        
        