# Objective: Return the index of the peak in a "mountain" array
# (in which the data points form the shape of a single spike)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range( len(arr) ):
            if arr[i] > arr[i+1]:
                return i
