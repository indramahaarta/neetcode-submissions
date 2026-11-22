class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        permutation = self.permute(nums[1:])
        opt = []
        for perm in permutation:
            p = perm[:]
            for i in range(len(perm) + 1):
                t = []
                t.extend(p[:i])
                t.append(nums[0])
                t.extend(p[i:])

                opt.append(t)
        
        return opt
                
        