def solution(L, word, pw_now, index):
    
    if len(pw_now) == L:
        if check(pw_now) == True:
            print(''.join(pw_now))
        return
    
    if index >= len(word):
        return

    solution(L, word, pw_now + list(word[index]), index + 1)
    solution(L, word, pw_now, index + 1)

        
def check(pw_now):
    #모음 , 자음
    a = 0
    b = 0

    for ch in pw_now:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            a += 1
        else:
            b += 1
    
    if b >= 2 and a >= 1:
        return True
    else:
        return False


L, C = map(int, input().split())
word = list(map(str, input().split()))
word.sort()
pw_now = []
index = 0

solution(L, word, pw_now, index)