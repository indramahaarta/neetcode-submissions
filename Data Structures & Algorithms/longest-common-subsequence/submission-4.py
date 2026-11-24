class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        
        def helper(i, j):
            nonlocal dp

            if i >= len(text1) or j >= len(text2):
                return 0
            
            if dp[i][j] > -1:
                return dp[i][j]

            x = 0
            if text1[i] == text2[j]:
                x = 1 + helper(i+1, j+1)
            else:
                x = max(helper(i+1, j), helper(i, j+1))

            dp[i][j] = x
            return x

        
        
        return helper(0, 0)


        