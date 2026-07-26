class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for i in strs:
            es += str(len(i)) + "#" + i
        
        return es 

    def decode(self, s: str) -> List[str]:
        k = 0
        res = []
        while k < len(s):
            start = k
            while k < len(s) and s[k] != '#':
                k += 1
            print(s[start:k])
            num = int(s[start:k])
            k += 1
            val = s[k:k+num]
            res.append(val)
            k += num

        return res
            # 2#ab3#abc