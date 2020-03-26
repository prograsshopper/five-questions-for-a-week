# Runtime: 696 ms, faster than 71.95% of Python3 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from math import sqrt
        distance_list = [[i, sqrt(elem[0]**2 + elem[1]**2)] for i, elem in enumerate(points) ]
        distance_list = sorted(distance_list, key=lambda distance: distance[1])[:K]
        result = [points[elem[0]] for elem in distance_list]
        return result
