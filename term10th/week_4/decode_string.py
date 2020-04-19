# https://leetcode.com/problems/decode-string/

def decodeString(s):
    stack = []
    num = 0
    temp_str = ''
    for elem in s:
        if elem == '[':
            stack.append(temp_str)
            stack.append(num)
            temp_str = ''
            num = 0
        elif elem == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            temp_str = prev_str + prev_num*temp_str
        elif elem.isdigit():
            num = num*10 + int(elem)
        else:
            temp_str += elem
    return temp_str
