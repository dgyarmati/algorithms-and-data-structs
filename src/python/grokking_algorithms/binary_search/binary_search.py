import math


def binary_search(values, n):
    lo = 0
    hi = len(values) - 1

    while lo <= hi:
        mid = math.floor((lo + hi) / 2)
        guess = values[mid]
        if guess > n:
            hi = mid - 1
        elif guess < n:
            lo = mid + 1
        else:
            return mid
