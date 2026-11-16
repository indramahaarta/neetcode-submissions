class Solution:
    def isHappy(self, n: int) -> bool:

        res = n
        while True:
            temp = res
            cur = 0
            while temp > 0:
                l = temp%10
                cur += l**2
                temp = temp//10
            
            res = cur
            
            if res < 10:
                break
        
        return res == 1

        