def solution(new_id):
    answer = ''

    # 1단계 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 문자 제거
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3단계 마침표가 2번이상 연속된 부분을 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계 마침표가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.')

    # 5단계 빈 문자열이라면 a 대입
    if len(answer) == 0:
        answer = 'a'

    # 6단계 길이가 16자 이상이라면 첫 15개의 문자를 제외한 나머지 문자를 모두 제거.
    # 만약 제거후 마침표가 new_id 끝에 위치한다면 마지막 마침표 제거

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계 길이가 2 이하라면 new_id의 마지막 문자를 길이가 3이 될때까지 반복해서 붙임
    while len(answer) < 3:
        answer += answer[-1]

    return answer
