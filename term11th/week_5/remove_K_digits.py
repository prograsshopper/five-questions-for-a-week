class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) == k:
            return str(0)
        stack = []
        for i in range(0, len(num)):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        # return "".join(stack).lstrip('0') or '0'
        return ''.join(stack[:-k or None]).lstrip('0') or '0'