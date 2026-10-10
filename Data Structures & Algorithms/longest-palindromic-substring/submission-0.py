class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        x, y = -1, -1
        N = len(s)

        for i in range(N):
            # odd
            l, r = i, i
            while l >=0 and r < N and s[l] == s[r]:
                curl = r - l + 1
                if curl > longest:
                    x = l
                    y = r
                    longest = curl
            
                l -= 1
                r += 1
            
            # even
            l , r = i, i+1
            while l >=0 and r < N and s[l] == s[r]:
                curl = r - l + 1
                if curl > longest:
                    x = l
                    y = r
                    longest = curl
            
                l -= 1
                r += 1
        
        return s[x:y+1]


        