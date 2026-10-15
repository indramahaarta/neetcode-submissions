class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tm = defaultdict(int)
        tm2 = defaultdict(int)
        need = 0
        for k in t:
            tm[k] += 1
            need += 1
        
        have = 0

        l = -1
        res = ""
        for r in range(len(s)):
            if s[r] in tm:
                l = r if l == -1 else l

                tm2[s[r]] += 1
                if tm2[s[r]] <= tm[s[r]]:
                    have += 1
                
                if have < need:
                    continue

                while need == have:
                    res = s[l:r+1] if (len(res) >= len(s[l:r+1]) or res == "") else res
                    if s[l] in tm2:
                        if tm2[s[l]] <= tm[s[l]]:
                            have -= 1
                        tm2[s[l]] -= 1

                    l += 1
                
                while l < len(s) and s[l] not in tm2:
                    l += 1
        
        return res
                        



                    



                


        