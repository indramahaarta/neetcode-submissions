class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input = [30, 38, 30, 36, 35, 40, 28]
        # stack = [] # will contain tuple of (input_i, index)
        # list = [0, 0, ..., 0]

        """
            1st:
                input_i, index = 30, 0
                stack = [(30, 0)]
                list = [0, 0, 0, 0, 0, 0, 0]
            
            2nd:
                input_i, index = 38, 1
                stack = [(38, 1)]
                list = [1, 0, 0, 0, 0, 0, 0]
            
            3rd:
                input_i, index = 30, 2
                stack = [(38, 1), (30, 2)]
                list = [1, 0, 0, 0, 0, 0, 0]
            
            4th:
                input_i, index = 36, 3
                stack = [(38, 1), (36, 3)]
                list = [1, 0, 1, 0, 0, 0, 0]

            5th:
                input_i, index = 35, 4
                stack = [(38, 1), (36, 3), (35, 4)]
                list = [1, 0, 1, 0, 0, 0, 0]

            6th:
                input_i, index = 40, 5
                stack = [(38, 1), (36, 3), (35, 4)]
                list = [1, 4, 1, 2, 1, 0, 0]
            
            7th:
                input_i, index = 28, 6
                stack = [(40, 5)]
                list = [1, 4, 1, 2, 1, 0, 0]
            
            Time complexity = number of iterration
                            = O(n)

        """
        N = len(temperatures)
        stack = [] # ()
        res = [0] * N

        for i in range(N):
            cur_temp = temperatures[i]
            # print(cur_temp, i, stack, res)
            while len(stack) != 0:
                val, idx = stack[-1]
                if cur_temp > val:
                    stack.pop()
                    res[idx] = i - idx
                else:
                    break
            stack.append((cur_temp, i))
        
        return res

        
        