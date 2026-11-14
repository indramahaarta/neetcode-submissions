class Solution:
    def expand(self, s: str) -> List[str]:
        l = s.split("}")

        l2 = []
        for i in range(len(l)):
            l2.append(l[i].split("{"))

        l = []
        for i in l2:
            for j in i:
                if j == "":
                    continue
                
                x = j.split(",")
                l.append(x)
        
        res = []
        def helper(i, cur):
            nonlocal res

            if i == len(l):
                res.append(cur)
                return

            for j in l[i]:
                temp = cur
                cur = cur + j
                helper(i+1, cur)
                cur = temp

        helper(0, "")

        return res

        