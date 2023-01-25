# Objective: Find the minimum cost of moving a robot to a certain position based on given information.

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        start_x = startPos[0]
        start_y = startPos[1]
        end_x = homePos[0]
        end_y = homePos[1]
        
        # Find minimum cost for row movement
        if start_x < end_x:
            rowsum = sum( rowCosts[start_x+1:end_x+1] )
        elif start_x > end_x:
            rowsum = sum( rowCosts[end_x:start_x] )
        else:
            rowsum = 0
        
        # Find minimum costs for column movement
        if start_y < end_y:
            colsum = sum( colCosts[start_y+1:end_y+1] )
        elif start_y > end_y:
            colsum = sum( colCosts[end_y:start_y] )
        else:
            colsum = 0
        
        mintotal = rowsum + colsum # add minimums for total

        return mintotal
