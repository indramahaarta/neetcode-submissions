class Solution:
    def reverseBits(self, n: int) -> int:
        s = 0

        c = 31
        while n > 0:
            tail = n % 2
            if tail:
                s += pow(2, c)
            n = n >> 1
            c -= 1
        
        return s

        