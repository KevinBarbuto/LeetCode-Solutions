# Objective: Given an array, return the maximum possible sum that
# can be obtained from the minimum of any combination of value pairings.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list
        nums.sort()

        # Find sum
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        
        return sum
