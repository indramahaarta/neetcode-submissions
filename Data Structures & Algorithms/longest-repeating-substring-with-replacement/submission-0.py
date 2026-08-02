class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = {}
        curMax = 0

        for r in range(len(s)):
            m[s[r]] = 1 + m.get(s[r], 0)

            while (r-l+1-max(m.values())) > k:
                m[s[l]] -= 1
                l += 1 
            
            curMax = max(curMax, r-l+1)
        
        return curMax
            



        