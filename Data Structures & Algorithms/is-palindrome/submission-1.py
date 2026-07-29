class Solution:
    def isPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1

        while a < b:
            while a < len(s) and not ((s[a] >= 'a' and s[a] <= 'z') or 
                (s[a] >= 'A' and s[a] <= 'Z') or
                (s[a] >= '0' and s[a] <= '9')
            ):
                a += 1
            
            while b >= 0 and not ((s[b] >= 'a' and s[b] <= 'z') or 
                (s[b] >= 'A' and s[b] <= 'Z') or
                (s[b] >= '0' and s[b] <= '9')
            ):
                b -= 1
            
            if a < b and s[a].lower() != s[b].lower():
                return False
            
            a += 1
            b -= 1

        return True
        