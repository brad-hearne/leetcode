# Python 3.6.5
# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from helper import timer

# Two pass scenario brute force
@timer
def twoSum(nums, target):
        # Iterate over first list
        for idx1, val1 in enumerate(nums):
            # Iterate over second list
            for idx2, val2 in enumerate(nums):
                check = val1 + val2
                #print(check)
                # Check value
                if check == target:
                    #print(idx1)
                    #print(idx2)
                    return [idx1, idx2]

print(twoSum([2,7,11,15], 9))


# Two pass scenario hash table
@timer
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]] 

print(twoSum([2,7,11,15], 9))

# One pass scenario hash table
@timer
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

print(twoSum([2,7,11,15], 9))