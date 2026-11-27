class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            swift = math.floor(math.log(i, 2))
            diff = int(i - math.pow(2, swift))
            t = i ^ diff
            a = 0 if t == 0 else 1
            res.append(res[diff] + a)
        
        return res
        


        