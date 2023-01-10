# Objective: Given a list of "stones" and "jewels", write a function that
# returns the number of "stones" that are considered "jewels"

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Initial number of duplicates found
        count = 0

        # Go through the list of stones and check them with jewels
        for i in stones:
            if i in jewels:
                count += 1
        return count
