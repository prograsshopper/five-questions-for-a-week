class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        visited = set()
        counter, n = 0, len(M)
        for i in range(0, n):
            if i not in visited:
                self.dfs(M, i, visited)
                counter += 1
        return counter
    def dfs(self, M, i, visited):
        visited.add(i)
        for idx in range(0, len(M[i])):
            if M[i][idx] == 1 and idx not in visited:
                self.dfs(M, idx, visited)
