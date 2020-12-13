import collections

def solution(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    answer = p - c
    return list(answer.keys())[0]

ans = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(list(ans.keys())[0])