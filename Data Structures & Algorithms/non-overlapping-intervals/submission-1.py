class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        opt = 0
        now = []
        intervals.sort()
        # print(intervals)
        for i in range(1, len(intervals)):
            # print(now)
            px, py = intervals[i-1][0], intervals[i-1][1]
            if now:
                px, py = now[0], now[1]

            x, y = intervals[i][0], intervals[i][1]

            if py > x:
                if py > y:
                    now = [x, y]
                else:
                    now = [px, py]
                opt += 1
            else:
                now = [x,y]
        
        return opt

        
        