def solution(seoul):
    i = 0
    for i, name in enumerate(seoul):
        if name == "Kim":
            return "김서방은 {}에 있다".format(i)
