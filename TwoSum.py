// Two Sum

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

def twoSum(nums, target):
    seen = {}  # value -> index

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i


// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]


