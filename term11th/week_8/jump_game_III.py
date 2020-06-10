class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        reach_dict = dict()
        for i in range(0, len(arr)):
            prev = i - arr[i]
            tail = i + arr[i]
            reach_dict[i] = list()
            if prev >= 0:
                reach_dict[i].append(prev)
            if tail < len(arr):
                reach_dict[i].append(tail)


        qu = []
        done = set()

        qu.append(start)
        done.add(start)

        while qu:
            current = qu.pop(0)
            for e in reach_dict[current]:
                if arr[e] == 0:
                    return True
                if e not in done:
                    qu.append(e)
                    done.add(e)
        return False