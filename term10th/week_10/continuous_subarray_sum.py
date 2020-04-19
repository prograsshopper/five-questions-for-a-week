class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_dict = {0:-1}
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            curr_sum = curr_sum % k if k else curr_sum
            if curr_sum in rem_dict:
                if i - rem_dict[curr_sum] > 1:
                    return True
            else:
                rem_dict[curr_sum] = i
        return False