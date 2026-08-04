class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        temp = []
        def dfs(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            
            # don't use
            dfs(i+1)

            # user
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
        
        dfs(0)

        return res
        