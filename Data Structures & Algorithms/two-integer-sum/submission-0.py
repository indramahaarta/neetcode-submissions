from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            k = nums[i]
            diff = target - k
            if diff in hm:
                return [hm[diff] ,i]

            hm[k] = i

        