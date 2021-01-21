def solution(answers):
    answer = []

    count_1 = 0
    count_2 = 0
    count_3 = 0
    first_ans = [1, 2, 3, 4, 5]
    second_ans = [2, 1, 2, 3, 2, 4, 2, 5]
    third_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first_ans[i % len(first_ans)]:
            count_1 += 1
        if answers[i] == second_ans[i % len(second_ans)]:
            count_2 += 1
        if answers[i] == third_ans[i % len(third_ans)]:
            count_3 += 1

    tmp = [count_1, count_2, count_3]
    for person, score in enumerate(tmp):
        if score == max(tmp):
            answer.append(person+1)
    return answer
