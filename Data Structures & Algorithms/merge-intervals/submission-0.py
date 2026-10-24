class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals, key = lambda i: (i[0], i[1]))
        res = []

        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                res.append(intervals[i])
            i += 1
        res.append(intervals[-1])
        return res
        