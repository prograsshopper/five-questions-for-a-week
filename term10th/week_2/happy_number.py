def solution(n):
    seen = dict()
    while n != 1:
        n = sum(int(num)**2 for num in str(n))
        if n in seen:
            return False
        else:
            seen[n] = True
    return True