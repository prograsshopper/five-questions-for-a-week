def get_palindrome(l, r , s):
    while l >=0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

def longestPalindrome(s):
    result = ""
    for i in range(0, len(s)):
        # 홀수
        curr_str = get_palindrome(i, i, s)
        if len(result) < len(curr_str):
            result = curr_str
        curr_str = get_palindrome(i, i+1, s)
        if len(result) < len(curr_str):
            result = curr_str
