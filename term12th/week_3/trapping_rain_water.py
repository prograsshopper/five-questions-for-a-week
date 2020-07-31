class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1, len(height)-1):
            left = max(height[:i])
            right = max(height[i+1:])
            current_sum = 0
            high = 0
            if left > right:
                high = right
            else:
                high = left
            if high > height[i]:
                current_sum = high - height[i]
                total += current_sum
        return total