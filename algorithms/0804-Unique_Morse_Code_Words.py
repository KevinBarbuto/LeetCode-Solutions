# Objective: Count the number of unique morse code strings from an array of given strings.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        result = []
        for word in words:
            morse = ""
            for char in word:
                morse += morse_code[ ord(char) - 97 ] # Convert to alphabetical
            
            # Ignore duplicates
            if morse not in result:
                result.append(morse)

        return len(result)
