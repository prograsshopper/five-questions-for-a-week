# Brutal   
def solution_one(s):
    if len(s) < 1:
        return 0
    max_repeat = 1
    for i in range(0, len(s)-1):
        repeat = 1
        for j in range(i+1, len(s)):
            if s[j] not in s[i:j]:
                repeat += 1
            max_repeat = max(max_repeat, repeat)
            if s[j] in s[i:j]:
                break
    return max_repeat

def solution_two(s):
    check_dict = {}
    start = 0
    answer = 0
    for i in range(0, len(s)):
        if s[i] in check_dict:
            answer = max(answer, i-start)
            start = max(start, check_dict[s[i]]+1)
        check_dict[s[i]] = i
    return max(answer, len(s)-start)

if __name__ == "__main__":
    print(solution_two("au")) # 2
    print(solution_two("abcabcbb")) # 3
    print(solution_two("")) # 0
    print(solution_two("bbbbb")) # 1
    print(solution_two("pwwkew")) # 3
    print(solution_two("dvdf")) # 3
