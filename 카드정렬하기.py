# N = int(input())

# num_list = list()
# for i in range(N):
#     num = int(input())
#     num_list.append(num)

# num_list.sort()

# res = 0
# while len(num_list) != 1:
#     least = num_list.pop(0)
#     sec_least = num_list.pop(0)

#     sum_value = least + sec_least
#     num_list.append(sum_value)
#     num_list.sort()
#     res += sum_value

# print(res)

import heapq

N = int(input())

num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)

res = 0
heapq.heapify(num_list)
while len(num_list) != 1:
    first = heapq.heappop(num_list)
    second = heapq.heappop(num_list)
    sum_value = first + second
    heapq.heappush(num_list, sum_value)
    res += sum_value

print(res)
