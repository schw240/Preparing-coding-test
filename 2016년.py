def solution(a, b):
    answer = ''
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day = (sum(months[:a-1]) + b) % 7
    print(day)
    answer = days[day]
    return answer
