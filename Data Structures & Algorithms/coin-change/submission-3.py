class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for j in coins:
                if i-j >= 0 and dp[i-j] != float('inf'):
                    dp[i] = min(dp[i], dp[i-j]+1)
        # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1