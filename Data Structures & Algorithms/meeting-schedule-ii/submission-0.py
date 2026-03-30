import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        heap = []
        heapq.heappush(heap,intervals[0].end)

        for meeting in intervals[1:]:
            if meeting.start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,meeting.end)
        
        return len(heap)
        