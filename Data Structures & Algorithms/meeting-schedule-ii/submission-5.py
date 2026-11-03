"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def minoverlapInterval(intervals):
            res = []
            if not intervals:
                return res
            intervals.sort(key = lambda i : i.start)
            prevEnd = intervals[0].end
            for i in intervals[1:]:
                if i.start >= prevEnd:
                    prevEnd = i.end
                else:
                    res.append(i)
            return res
        days = 0
        res = intervals
        while(res):
            days += 1
            res = minoverlapInterval(res)
        return days if intervals else 0
