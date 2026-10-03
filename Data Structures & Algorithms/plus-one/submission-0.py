class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        digits = [7, 8, 1, 0]
                  0  1  2  3  

        len(digits) = 4
        """

        # kode untuk reverse
        # temp itu isinya digits yang di-reverse
        digits.reverse()
        
        res = []
        leftover = 1
        for digit in digits:
            curValue = leftover + digit

            curValueWillBeAdded = curValue
            if curValueWillBeAdded >= 10:
                curValueWillBeAdded = curValueWillBeAdded - 10
            leftover = curValue // 10
            res.append(curValueWillBeAdded)

        if leftover:
            res.append(leftover)
        
        res.reverse()

        return res