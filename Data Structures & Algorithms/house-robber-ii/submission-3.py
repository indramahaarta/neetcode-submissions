class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n1 = nums[:-1]
        n2 = nums[1:]
        mx1 = [0]*len(n1)
        mx2 = [0]*len(n2)

        for i in range(len(n1)):
            if i-2 >= 0:
                mx1[i] = max(mx1[i-1], mx1[i-2] + n1[i])
                continue
            
            mx1[i] = max(n1[:i+1])
        
        for i in range(len(n2)):
            if i-2 >= 0:
                mx2[i] = max(mx2[i-1], mx2[i-2] + n2[i])
                continue
            
            mx2[i] = max(n2[:i+1])

        # print(mx1, mx2)
        
        return max(mx1[-1], mx2[-1])
        