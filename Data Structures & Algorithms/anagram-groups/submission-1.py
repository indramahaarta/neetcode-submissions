from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # [[1,0,...0] => ['act', 'cat', ..], ...]

        for val in strs:
            l = [0]*26

            for c in val:
                l[ord(c)-ord("a")] += 1
            
            d[tuple(l)].append(val)
        
        return list(d.values())
        




        