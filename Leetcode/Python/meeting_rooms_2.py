import heapq
List = list
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort(key=lambda interval : interval[0])
        end = []
        minRooms = 0
        for interval in intervals:
            s, e = interval
            while len(end) > 0 and end[0] <= s:
                heapq.heappop(end)
            heapq.heappush(end, e)
            minRooms = max(minRooms, len(end))
        return minRooms