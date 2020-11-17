class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # time exceed
        from itertools import product
        result = 0
        all_combis = product('+-', repeat=len(nums))
        for combi in all_combis:
            total = 0
            for i in range(len(combi)):
                if combi[i] == '+':
                    total += nums[i]
                else:
                    total -= nums[i]
            if total == S:
                result += 1
        return result