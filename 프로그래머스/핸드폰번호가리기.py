def solution(phone_number):
    answer = ''
    stars = '*' * (len(phone_number) - 4)
    answer += stars + phone_number[-4:]
    return answer
