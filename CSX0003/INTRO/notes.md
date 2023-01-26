# Divide and conquer paradigm
- Divide into smaller subproblems
- Conquer -> recursion
- Combine solutions of subproblems into the original problem

# Merge sort

## O: nlog(n) ?
## Space: n

## Input: Array of n numbers, unsorted

## Output: Array of n numbers sorted in increasing order

## Pseudocode:
#### input_array: len(n)
#### left_array_sorted: len(n/2)
#### right_array_sorted: len(n/2)
#### output_array: len(n)
- Recursively:
- Divide array in half
    - If array is 0/1 elements, consider it sorted and return
    - Traverse through sorted arrays
    - The minimum element that you haven't visited in lef or right sorted, should be the next item to push to the final array
        - a < b -> c[k] = a[i]; i++
        - b < a -> c[k] = b[j]; j++
    - k++

# Counting inversions

## O:
## Space:

## Input: Array with numbers in arbitrary order
## Output: Number of pairs of array indices with i < j & first number greater than second number

## Example 
## Input: (1,3,5,2,4,6)
## Inversions
- (3,2), (5,2), (5,4), 

## Principle: Largest number of inversions: (n(n-1)/2)


### Approach
- Inversion Array with i < j
- left if i,j less or eq than half length
- right if i,j more than half length
- split if i less or eq than half and j greater than half

## High level algorithm

- Base case -> length 1 return 0
- else:
    - sorted_B, x = sortAndCount(left half, length / 2)
    - sorted_C, y = sortAndCount(right half, length / 2)
    - sorted_D, z = mergeAndCountSplitInversions(sorted_B, sorted_C, length)
- return x+y+z

### Goal implement z function in O(n) to have O(n)log(n) complexity