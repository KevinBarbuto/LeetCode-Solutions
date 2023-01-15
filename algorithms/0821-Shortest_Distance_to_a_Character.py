# Objective: Given a string and a character, return a list 
# of the distance to that character from each position in the string

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Find index positions for c
        index_list = []
        for i in range( len(s) ):
            if s[i] == c:
                index_list.append(i)
        
        # Minimize distance between index and c
        answer = []
        for j in range( len(s) ):
            answer.append( min( abs(j-x) for x in index_list ) )
        return answer
