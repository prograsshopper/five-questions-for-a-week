import itertools

class Solution:
    def permute(self, nums):
        permutations_iterator = itertools.permutations(nums)
        result = [permutation for permutation in permutations_iterator]
        return result
