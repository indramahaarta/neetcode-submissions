class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        p = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            res[i+1] = p
        
        p = 1
        for i in range(len(nums)-1, 0, -1):
            p *= nums[i]
            res[i-1] *= p
        
        return res

        # prefix = [0]*len(nums)
        # sulfix = [0]*len(nums)

        # p = 1
        # for i in range(len(nums)):
        #     num = nums[i]
        #     p *= num
        #     prefix[i] = p
        
        # p = 1
        # for i in range(len(nums)-1, -1, -1):
        #     num = nums[i]
        #     p *= num
        #     sulfix[i] = p
        
        # res = []
        # for i in range(len(nums)):
        #     p, s = 1, 1
        #     if i > 0:
        #         p = prefix[i-1]
        #     if i < len(nums) - 1:
        #         s = sulfix[i+1]
        #     res.append(p*s)
        
        # return res

        