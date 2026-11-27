class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            swift = math.floor(math.log(i, 2))
            t = i >> swift
            diff = int(i - math.pow(2, swift))
            res.append(res[diff] + t)
        
        return res
        


        