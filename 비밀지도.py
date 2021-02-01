def solution(n, arr1, arr2):
    answer = []
    tmp = ""
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:]
        answer.append(
            ("0" * (n - len(tmp)) + tmp).replace("1", "#").replace("0", " "))
    print(answer)
    return answer
