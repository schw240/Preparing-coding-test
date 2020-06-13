'''
input

3
7
7 1 5 9 6 7 3
7
1 4 4 4 4 1 1 
4
1 8 2 2

output

20
16
8
'''
import sys

def fence(left, right, heights):
    if left == right:
        return heights[left]

    mid = (left+right)/2

    result = max(fence(left, mid, heights), fence(mid+1, right, heights))

    low = mid
    high = mid+1
    cur_height = min(heights[low], heights[high])

    result = max(result, cur_height * 2)

    while left < low or high < right:
        if high < right and (low == left or heights[low - 1] < heights[high + 1]):
            high += 1
            cur_height = min(cur_height, heights[high])
        else:
            low -= 1
            cur_height = min(cur_height, heights[low])

        result = max(result, cur_height * (high - low + 1))

    return result


if __name__ == '__main__':
    C = int(input())
    for i in range(C):
        N = int(input())
        heights = [int(x) for x in input().split()]
        sys.setrecursionlimit(2000)
        print(fence(0, N-1, heights))
