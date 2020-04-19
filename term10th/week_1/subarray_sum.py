# 1 Brute Force : Time Exceed
def subarraySum(nums, k):
        if len(nums) == 0:
            return 0
        if len(nums) <= 1:
            if sum(nums) == k:
                return 1
            return 0
        result = 0
        for i in range(0, len(nums)-1):
            current_sum = nums[i]
            if current_sum == k:
                result+=1
            for j in range(i+1, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    result += 1
            if i == len(nums) -2 and nums[i+1] == k:
                result += 1
        return result
