# naive, inefficient solution
# def quicksort(items):
#     if len(items) < 2:
#         return items
#     else:
#         pivot = items[0]
#         less = [i for i in items[1:] if i < pivot]
#         greater = [i for i in items[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


def quicksort(items, first_idx, last_idx):
    if first_idx < last_idx:
        pivot_idx = partition(items, first_idx, last_idx)
        quicksort(items, first_idx, pivot_idx - 1)
        quicksort(items, pivot_idx + 1, last_idx)

# TODO rewrite to use mid point as pivot
def partition(items, first_idx, last_idx):
    pivot_item = items[first_idx]

    lo_idx = first_idx + 1
    hi_idx = last_idx

    while True:

        while lo_idx <= hi_idx and items[lo_idx] <= pivot_item:
            lo_idx = lo_idx + 1

        while items[hi_idx] >= pivot_item and hi_idx >= lo_idx:
            hi_idx = hi_idx - 1

        if hi_idx < lo_idx:
            break
        else:
            items[lo_idx], items[hi_idx] = items[hi_idx], items[lo_idx]

    items[first_idx], items[hi_idx] = items[hi_idx], items[first_idx]

    return hi_idx
