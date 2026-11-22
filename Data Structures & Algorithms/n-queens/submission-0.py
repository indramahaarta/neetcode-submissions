class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def build(opt):
            nonlocal res
            # print(opt)
            temp = []
            for i in opt:
                s = ("." * i) + "Q" + ("." * (n-i-1))
                temp.append(s)
            res.append(temp)

        def helper(r = [], i = 0):
            # print(r, i)
            if i == n:
                # print(r)
                build(r)
                return
            
            for j in range(n):
                a = True
                if r:
                    for k in range(len(r)):
                        l = r[k]
                        if l == j or abs(k-i) == abs(l-j):
                            a = False
                            break
                
                if a:
                    r.append(j)
                    helper(r, i + 1)
                    r.pop()
    
        helper([], 0)
        return res
                        
                
            

