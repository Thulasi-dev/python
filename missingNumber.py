// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2   # Sum of numbers from 0 to n
    array_sum = sum(nums)
    return total_sum - array_sum


// Input: nums = [3,0,1]

// Output: 2
