# Code will not be able to run, inputs of list from leetcode
# Concepts: Hashmap
# TC: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Initialize Hashmap
        hashmap = {}
        # Loop the length of the list
        for i in range(len(nums)):
            # Compute the complement needed
            complement = target - nums[i]
            # Check if complement is already is the hashmap, if yes, return it's index
            if complement in hashmap:
                return(hashmap[complement], i)
            # if no, stores the current int in the hashmap
            hashmap[nums[i]] = i