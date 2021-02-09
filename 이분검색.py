def binsearch(n, S, target):
    low = 1
    high = n
    location = 0
    while (low <= high and location == 0):
        mid = (low + high) // 2
        if target == S[mid]:
            location = mid
        elif target < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return location


S = [5, 7, 8, 10, 11, 13]
x = 5
location = binsearch(len(S) - 1, S, x)
print(location)
