class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(ctr, r, c):
            if ctr == n:
                c += ")" * r
                r -= r
                res.append(c)
                return
            
            # Add (
            helper(ctr + 1, r + 1, c + "(")

            if r > 0:
                # Add )
                helper(ctr, r - 1, c + ")")
        
        helper(0, 0, "")
        return res
            



        