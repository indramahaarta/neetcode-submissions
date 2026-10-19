"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = []
        for i in intervals:
            l.append((i.start, i.end))
        sortedIntervals = sorted(l)
        for i in range(1, len(sortedIntervals)):
            a, b = sortedIntervals[i-1], sortedIntervals[i]

            if a[1] > b[0]:
                return False
        
        return True

