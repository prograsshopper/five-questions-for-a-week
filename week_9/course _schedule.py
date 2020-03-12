import collections

def canFinish1(self, numCourses, prerequisites):
    all_graph = {i: set() for i in range(0, numCourses+1)}
    prereq = collections.defaultdict(set)
    for i, j in prerequisites:
        all_graph[i].add(j)
        prereq[j].add(i)
    queue =  [elem for elem in all_graph if len(all_graph[elem]) == 0]
    while queue:
        current = queue.pop(0)
        for elem in prereq[current]:
            all_graph[elem].remove(current)
            if len(all_graph[elem]) == 0:
                queue.append(elem)
        all_graph.pop(current)
    return not all_graph