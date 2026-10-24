class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = -1
        res = []
        for i in range(len(intervals)):
            if s == -1:
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    res.append(intervals[i])
                    res.extend(intervals[i+1:])
                    return res
                elif newInterval[0] > intervals[i][1]:
                    res.append(intervals[i])
                else:
                    s = min(newInterval[0], intervals[i][0])
            elif s > -1 and newInterval[1] < intervals[i][0]:
                res.append([s, newInterval[1]])
                res.extend(intervals[i:])
                # print(res)
                return res
            elif s > -1 and newInterval[1] <= intervals[i][1]:
                res.append([s, intervals[i][1]])
                res.extend(intervals[i+1:])
                # print(res)
                return res
        if s == -1:
            res.append(newInterval)
        else:
            res.append([s, max(intervals[-1][1], newInterval[1])])
        return res
            





        