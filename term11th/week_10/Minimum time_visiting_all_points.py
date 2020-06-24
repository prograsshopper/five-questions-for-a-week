class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        prev = points.pop(0)
        while points:
            tail = points.pop(0)
            count += max(abs(prev[0] - tail[0]), abs(prev[1] - tail[1]))
            prev = tail
        return count