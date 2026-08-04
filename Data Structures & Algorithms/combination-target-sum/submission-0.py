class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        temp = []
        def dfs(i):
            if i >= len(nums):
                return 

            if sum(temp) > target:
                return
            
            if sum(temp) == target:
                res.append(temp.copy())
                return
            
            # choose i
            temp.append(nums[i])
            dfs(i)
            temp.pop()

            # don't choose i
            dfs(i+1)
        
        dfs(0)
        return res

        