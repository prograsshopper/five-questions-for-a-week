# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.createTree(nums)
    
    def createTree(self, nums):
        if not nums:
            return None
        max_num, max_idx = float('-inf'), -1
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = i
        
        root = TreeNode(max_num)
        root.left = self.createTree(nums[:max_idx])
        root.right = self.createTree(nums[max_idx+1:])
        return root