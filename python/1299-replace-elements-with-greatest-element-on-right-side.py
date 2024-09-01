# Takes an array and replaces each element with the largest value following it.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initital max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr
