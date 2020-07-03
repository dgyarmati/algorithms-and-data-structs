## Quicksort Notes

Ordering the elements around a pivot is called **partitioning**.

- worst case: O(n^2)
- average case: O(n log n)

(O(n log n) = O(n) which is the number of elements touched * O(log n) which is the height of the call stack)

Compared to merge sort, it has a worse average speed (merge sort is always O(n log n)), but
quicksort's constant is smaller, so it hits the average case much more often.

Picking the right pivot is hard: choosing the first or last element leads to worse performance on sorted or semi-sorted sequences. Quicksort can be optimized by picking the right pivot: the middle element.

To sum up, quick sort is better for small datasets and arrays, while merge sort is better for large data sets and linked lists.
Also, quick sort sorts in place, so does not require additional memory, while merge sort does.
