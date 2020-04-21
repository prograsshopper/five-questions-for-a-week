"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
"""
def increasingTriplet(self, nums):
    first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num<= second:
                second = num
            else:
                return True
        return False
