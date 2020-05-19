class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for alpha in S:
            if not stack or stack[-1] != alpha:
                stack.append(alpha)
            else:
                while stack and stack[-1] == alpha:
                    stack.pop()
        return "".join(stack)