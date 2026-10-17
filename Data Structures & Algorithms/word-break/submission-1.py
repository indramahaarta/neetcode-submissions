class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                l = len(word)
                # print(i, l)
                if i + l > len(s):
                    continue
                
                if s[i:i+l] == word and dp[i+l]:
                    dp[i] = True
                    break
            
            # print("\n")
        # print(dp)
        return dp[0]
        

        


        