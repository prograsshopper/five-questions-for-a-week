class Solution:
    def reverse(self, x: int) -> int:
        return_x = int(str(x)[::-1]) if x > 0 else int("-"+str(int(str(abs(x))[::-1])))
        if int(return_x) < (-2**31) or int(return_x) > (2**31-1):
            return 0
        return return_x