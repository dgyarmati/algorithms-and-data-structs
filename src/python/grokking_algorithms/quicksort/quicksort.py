# naive, inefficient solution
def quicksort(items):
    if len(items) < 2:
        return items
    else:
        pivot = items[0]
        less = [i for i in items[1:] if i < pivot]
        greater = [i for i in items[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
