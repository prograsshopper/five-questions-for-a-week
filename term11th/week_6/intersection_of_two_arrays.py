class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        num_dict = defaultdict(lambda:0)
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        result = []
        for num in (nums1+nums2):
            num_dict[num] += 1
            if num_dict[num] > 1:
                result.append(num)
        return result