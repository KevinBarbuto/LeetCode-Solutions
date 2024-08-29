# Objective: Given a list of integers "nums", return the element
# that appears most frequently.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} # Define hash table
        result = 0
        maxCount = 0

        # Iterate through list and add to hash table
        for n in nums:
            count[n] = count.get(n, 0) + 1 
            if count[n] > maxCount:
                result = n
            maxCount = max(count[n], maxCount)
        
        return result
