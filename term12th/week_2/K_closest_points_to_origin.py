class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from math import sqrt
        idx_dic = {}
        vals = []
        for i in range(0, len(points)):
            cur_val = sqrt(sum([elem ** 2 for elem in points[i]]))
            vals.append(cur_val)
            idx_dic[i] = cur_val        
        vals = sorted(vals)[:K]
        result = []
        for i in range(0, len(points)):
            if idx_dic[i] in vals and len(result) < K:
                result.append(points[i])
        return result

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from math import sqrt
        distance_list = [[i, sqrt(elem[0]**2 + elem[1]**2)] for i, elem in enumerate(points) ]
        distance_list = sorted(distance_list, key=lambda distance: distance[1])[:K]
        result = [points[elem[0]] for elem in distance_list]
        return result
