class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        pow = 1

        while i < len(nums):
            if pow == 0:
                return False

            pow -=1
            pow = max(pow, nums[i])
            
            i += 1 
        
        return True
        