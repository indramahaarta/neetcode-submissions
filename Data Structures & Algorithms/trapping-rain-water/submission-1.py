class Solution:
    def trap(self, height: List[int]) -> int:
        """
        ------------------------------------------------
            
            oo

            ooo
            o

            o
            ooo
            oo
            o
        ------------------------------------------------
        """

        L, R = 0, len(height)-1
        cur_max_l, cur_max_r = height[L], height[R]
        cur_water = 0

        while L < R and R - L >= 2:
            isL = False
            if height[L] < height[R]:
                isL = True
            
            h = 0
            if isL:
                L += 1
                h = height[L]
            else:
                R -= 1
                h = height[R]
            
            water = min(cur_max_l, cur_max_r) - h
            if water > 0:
                cur_water += water
            
            cur_max_l = max(cur_max_l, height[L])
            cur_max_r = max(cur_max_r, height[R])

                
        
        return cur_water




        