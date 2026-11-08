class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)

        if S % 2 == 1:
            return False
        
        A = S // 2

        DP = [{} for _ in range(len(nums))]

        def helper(i, r):
            # print(i, r)
            if i == len(nums):
                
                if r == 0:
                    return True
                else:
                    return False

            if r in DP[i]:
                return DP[i][r]
            
            if r >= nums[i]:
                DP[i][r] = helper(i+1, r - nums[i])
                if DP[i][r]: return True
            
            DP[i][r] = helper(i+1, r)
            return DP[i][r]
        
        ans = helper(0, A)
        # print(DP)

        return ans
        