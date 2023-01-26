## Merge sort principle

# O: nlog(n) ?
# Space: n

# Input: Array of n numbers, unsorted

# Output: Array of n numbers sorted in increasing order

# Pseudocode:
# input_array: len(n)
# left_array_sorted: len(n/2)
# right_array_sorted: len(n/2)
# output_array: len(n)
# - Recursively:
# - Divide array in half
# - If array is 0/1 elements, consider it sorted and return
# - Traverse through sorted arrays
# - The minimum element that you haven't visited in lef or right sorted, should be the next item to push to the final array
# - a < b -> c[k] = a[i]; i++
# - b < a -> c[k] = b[j]; j++
# - k++