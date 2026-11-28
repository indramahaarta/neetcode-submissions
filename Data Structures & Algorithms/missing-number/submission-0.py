class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range (1, len(nums) + 1):
            xor = xor ^ i
        
        for i in nums:
            xor = xor ^ i
        
        return xor
        