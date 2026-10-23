"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])

        res, count = 0, 0
        sp, ep = 0, 0
        while sp < len(s):
            if s[sp] < e[ep]:
                count += 1
                sp += 1
            else:
                count -= 1
                ep += 1
        
            res = max(res, count)
        
        return res
