def binsearch(S, low, high):
    if low > high:
        return 0
    else:
        mid = (low+high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return binsearch(S, low, mid-1)
        else:
            return binsearch(S, mid+1, high)
