## A Note on Big O

Selection sort is twice as fast for, say, ten elements, than bubble sort: both has comparisons and swaps, but selection sort
swaps for one passthrough, while bubble sort swaps for each step. That would make selection sort speed O(N^2/2), while bubble
sort O(N^2). However, big O ignores constants, that is, numbers that are not exponents, because it takes into account the long-
term growth: on larger datasets, they both perform about the same. 