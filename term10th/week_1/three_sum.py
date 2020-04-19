def threeSum(nums):
    nums.sort()
    result = []
    end = len(nums)-1
    for i in range(end, 1, -1):
        if i != end and nums[i] == nums[i+1]:
            continue
        current = nums[i]
        target_val = -current
        j = 0
        k = i-1
        while j<k:
            first = nums[j]
            last = nums[k]
            if first + last > target_val:
                k -= 1
            elif first + last < target_val:
                j += 1
            else:
                elem = [current, first, last]
                result.append(elem)
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                k -= 1

    return result
