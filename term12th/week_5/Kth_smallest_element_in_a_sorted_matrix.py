class Solution:
    # first solution: passed
    # 한 줄로 만들 수 있음: return sorted([ele for row in matrix for ele in row])[k-1]
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        total = []
        for i in range(0, len(matrix)):
            total += matrix[i]
        total.sort()
        return total[k-1]
    
    # second solution: using heap
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        heap = []
        for elem in matrix:
            heap += elem
        heapq.heapify(heap)
        res = None
        for i in range(0, k):
            res = heapq.heappop(heap)
        return res
