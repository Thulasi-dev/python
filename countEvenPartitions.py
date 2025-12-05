// Count partitions with even sum difference

"""
You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even. """

def countEvenPartitions(nums):
    total_sum = sum(nums)
    
    # If total sum is odd, no partition can give even difference
    if total_sum % 2 != 0:
        return 0
    
    # If total sum is even, ALL partitions (0 to n-2) are valid
    return len(nums) - 1


// Input: nums = [10,10,3,7,6]
// Output: 4

// Input: nums = [1,2,2]
// Output: 0
