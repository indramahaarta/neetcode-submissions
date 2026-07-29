class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        ooooooo
        o
        ooooooo
        oo
        oo
        oooo
        """

        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append((i, height))
                continue
            
            l_i = i
            while stack:
                t_i, t_height = stack[-1]
                if t_height <= height:
                    break

                x, y = i - t_i, t_height
                max_area = max(max_area, x*y)
                l_i = t_i
                stack.pop()
            
            stack.append((l_i, height))

        # print(stack, max_area)
        
        if stack:
            l_i = len(heights)
            for i, v in stack:
                max_area = max(max_area, v *(l_i-i))
        

        return max_area 


        