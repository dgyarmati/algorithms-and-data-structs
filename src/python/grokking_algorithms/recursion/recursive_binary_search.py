def binary_search(items, n, lo=0, hi=None):
    if hi is None:
        hi = len(items) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    if items[mid] == n:
        return mid
    elif items[mid] < n:
        return binary_search(items, n, mid+1, hi)
    elif items[mid] > n:
        return binary_search(items, n, lo, mid-1)
