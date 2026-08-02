class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        m = {}
        for i in s1:
            m[i] = 1 + m.get(i, 0)
        
        n = len(s1)
        m2 = {}
        c = 0
        for i in range(len(s2)):
            if c < n:
                c += 1
                m2[s2[i]] = 1 + m2.get(s2[i], 0)
                continue
            
            # print(m, m2)
            if m == m2:
                return True

            l = i-n
            m2[s2[l]] -= 1
            if m2[s2[l]] <= 0:
                del m2[s2[l]]
            m2[s2[i]] = 1 + m2.get(s2[i], 0)
        
        if m == m2:
            return True
        
        return False

        


        