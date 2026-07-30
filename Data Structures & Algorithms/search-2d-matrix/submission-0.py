class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            a, b = matrix[mid][0], matrix[mid][-1]

            if target < a:
                r -= 1
            elif target > b:
                l += 1
            elif target >= a and target <= b:
                matrix_mid = matrix[mid]
                l, r = 0, len(matrix_mid) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix_mid[mid] == target:
                        return True
                    elif matrix_mid[mid] > target:
                        r -= 1
                    else:
                        l +=1 
        
        return False

        