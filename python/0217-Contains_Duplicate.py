# Objective: Write a function that will take a list "nums" and return a 
# boolean value indicating whether or not the list contains any duplicate values.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Sort the list numerically
        nums.sort()

        # Move through the list and test each value against the next one
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
