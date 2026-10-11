class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0]*(N+1)
        dp[-1] = 1
        
        for i in range(N-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i + 1 < N and (
                (s[i] == "1" and s[i+1] in "0123456789") or 
                (s[i] == "2" and s[i+1] in "0123456")
            ):
                dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]


        