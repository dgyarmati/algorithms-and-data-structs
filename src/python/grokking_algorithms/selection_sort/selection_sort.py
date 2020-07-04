# def selection_sort(values):
#     sorted_values = []
#     for i in range(len(values)):
#         smallest_idx = find_smallest(values)
#         sorted_values.append(values.pop(smallest_idx))
#     return sorted_values
#
#
# def find_smallest(values):
#     smallest = values[0]
#     smallest_idx = 0
#     for i in range(1, len(values)):
#         if values[i] < smallest:
#             smallest = values[i]
#             smallest_idx = i
#     return smallest_idx


#  O(n^2) time complexity
def selection_sort(items):
    for i in range(len(items)):
        min_item_idx = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_item_idx]:
                min_item_idx = j

        if min_item_idx != i:
            items[i], items[min_item_idx] = items[min_item_idx], items[i]
