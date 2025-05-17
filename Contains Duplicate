# Brute Force Approach to confirm there's a solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n): # For Loop is nested so when i=0 it'll check against all the other j inner loop will run finish before second loop of outer loop
                if nums[i] == nums[j]:
                    return True
        return False
