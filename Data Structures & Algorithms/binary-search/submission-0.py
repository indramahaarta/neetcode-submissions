class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        1 2 3 4 6 7 8 9
              ^ ^
        """

        l, r = 0, len(nums)
        while l < r:
            mid = (r + l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r -= 1
            else:
                l += 1
        
        return -1
        