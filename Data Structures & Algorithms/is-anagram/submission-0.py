from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = defaultdict(int), defaultdict(int)

        for i in s:
            h1[i] += 1
        
        for i in t:
            h2[i] += 1
        
        return h1 == h2

        