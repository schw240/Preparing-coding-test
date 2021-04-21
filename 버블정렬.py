"""
1. for num in range(len(data_list)) 반복
2. swap = 0 
3. 반복문 안에서 for index in range(len(data_list) - num - 1) n-1 번 반복
4. 반복문안의 반복문 안에서, if data_list[index] > data_list[index + 1]이면 
5. data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
6. swap += 1
7. 반복문 안에서 if swap == 0 이면 break
"""


def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]

        if swap == False:
            break

    return data
