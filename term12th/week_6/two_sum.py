class Solution:
    # old version
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            remain = target - nums[i]
            for j in range(i+1, len(nums)):
                if remain == nums[j]:
                    return [i, j]
    
    # new - use hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[target - nums[i]] = i
            else:
                return num_dict[nums[i]], i
