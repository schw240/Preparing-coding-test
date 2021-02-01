def solution(s):
    new_s = s.split(" ")
    answer = ""
    for word in new_s:
        for i, ch in enumerate(word):
            answer += ch.upper() if i % 2 == 0 else ch.lower()
        answer += " "
    return answer[:-1]
