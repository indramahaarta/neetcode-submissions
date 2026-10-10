class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        total = 0

        for i in range(N):
            # odd
            l, r = i, i
            while l >=0 and r < N and s[l] == s[r]:
                total += 1
            
                l -= 1
                r += 1
            
            # even
            l , r = i, i+1
            while l >=0 and r < N and s[l] == s[r]:
                total += 1
            
                l -= 1
                r += 1
        
        return total