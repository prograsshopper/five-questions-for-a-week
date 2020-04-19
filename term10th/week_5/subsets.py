import itertools
class Solution:
    def subsets(self, nums):
        result = []
        for i in range(0, len(nums)+1):
            combi_iter = itertools.combinations(nums, i)
            for combi in combi_iter:
                result.append(combi)
        return result
