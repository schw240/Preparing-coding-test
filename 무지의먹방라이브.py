from queue import PriorityQueue


def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    answer = 0

    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)
    # print(q.queue)

    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q.queue, key=lambda x: x[1])
    return result[(k - sum_value) % len(q.queue)][1]
