class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            for j in range(0, i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        nums = [str(num) for num in nums]
        return str(int("".join(nums)))

    def compare(self, h, t):
        return str(h)+str(t) > str(t)+str(h)