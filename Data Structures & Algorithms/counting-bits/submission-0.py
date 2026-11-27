class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 - 1 1 2 log 0
        2 - 3 2
        4 - 7 3
        8 - 15 4
        """

        res = [0]
        for i in range(1, n+1):
            swift = math.floor(math.log(i, 2))
            t = i >> swift
            diff = int(i - math.pow(2, swift))
            # print(diff)
            res.append(res[diff] + t)
        
        return res
        


        