class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        d = {}
        ctr = ord("a")
        for i in range(2, 10):
            d[i] = []
            match i:
                case 7 | 9:
                    for j in range(4):
                        d[i].append(chr(ctr))
                        ctr += 1
                case _:
                    for j in range(3):
                        d[i].append(chr(ctr))
                        ctr += 1

        opt = []
        def helper(s, cur):
            if cur == len(digits):
                opt.append(s)
                return
            
            num = int(digits[cur])
            for i in d[num]:
                t = s
                t += i
                helper(t, cur + 1)
        
        helper("", 0)
        return opt

        