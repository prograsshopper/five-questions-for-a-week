class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        def helper(nums, target, start, end, my_dict):
            if target in my_dict:
                return my_dict[target]
            elif target == 0:
                my_dict[target] = True
            else:
                my_dict[target] = False
                if target > 0:
                    for i in range(start, end):
                        if helper(nums, target - nums[i], i+1, end, my_dict):
                            my_dict[target] = True
                            break
            return my_dict[target]
        return helper(nums, nums_sum//2, 0, len(nums), {})