class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return result
        intervals.sort()
        prev = intervals[0]
        intervals = intervals[1:]
        while intervals:
            current = intervals[0]
            if current[0] - prev[1] > 0:
                result.append(prev)
                prev = intervals[0]
            else:
                set_arr = prev + current
                new_elem = [min(set_arr), max(set_arr)]
                prev = new_elem
            intervals = intervals[1:]
        if len(result) == 0 or result[-1] != prev:
            result.append(prev)
        return result
