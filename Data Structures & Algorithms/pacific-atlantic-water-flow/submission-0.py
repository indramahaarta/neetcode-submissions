class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        set_pasific = set()
        set_atlantic = set()

        def dfs(x, y, is_pasific = True):
            if not (x >= 0 and x < len(heights)):
                return

            if not (y >= 0 and y < len(heights[0])):
                return

            if is_pasific and (x, y) in set_pasific:
                return
            
            if not is_pasific and (x, y) in set_atlantic:
                return
            
            if is_pasific:
                set_pasific.add((x, y))
            
            if not is_pasific:
                set_atlantic.add((x, y))
            
            directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for (xn, yn) in directions:
                if not (xn >= 0 and xn < len(heights)):
                    continue

                if not (yn >= 0 and yn < len(heights[0])):
                    continue

                if heights[x][y] > heights[xn][yn]:
                    continue

                dfs(xn, yn, is_pasific)
        
        for i in range(len(heights)):
            dfs(i, 0, True)
            dfs(i, len(heights[0])-1, False)
        
        for i in range(len(heights[0])):
            dfs(0, i, True)
            dfs(len(heights)-1, i, False)
        
        print(set_pasific, set_atlantic)
        res = []
        if len(set_atlantic) > len(set_pasific):
            set_pasific, set_atlantic = set_atlantic, set_pasific
            
        for (x, y) in set_pasific:
            if (x,y) in set_atlantic:
                res.append([x, y])

        return res
            

        