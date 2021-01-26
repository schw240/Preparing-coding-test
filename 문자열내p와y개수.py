def solution(s):
    answer = True
    num_p = 0
    num_y = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            num_p += 1
        elif s[i] == 'y':
            num_y += 1
    if num_p == num_y:
        return True
    else:
        return False
