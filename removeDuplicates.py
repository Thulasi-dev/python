// Remove Duplicates from Sorted Array

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
// The relative order of the elements should be kept the same.

// Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

// The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # points to position where next unique element should go

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:   # found a new unique element
            nums[k] = nums[i]        # place it at index k
            k += 1                   # move k forward

    return k


// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]


