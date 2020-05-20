class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        paren_idx = []
        for i in range(0, len(s)):
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    paren_idx.pop()
                else:
                    stack.append(s[i])
                    paren_idx.append(i)
            elif s[i] == '(':
                stack.append(s[i])
                paren_idx.append(i)
            else:
                pass
        
        result = ""
        for i in range(0, len(s)):
            if i in paren_idx:
                paren_idx.remove(i)
            else:
                result += s[i]
        return result