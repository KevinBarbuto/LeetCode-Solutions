# Objective: Take an Arabic numeral input and convert into Roman numerals.

class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Ordered list
        roman_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                     ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                     ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                     ["M", 1000]]
        
        result = "" # Placeholder string for result
        
        for symbol, value in reversed(roman_list):
            count = num // value # How many of each symbol is needed
            result += (count * symbol) # Add symbols to output
            num = num % value # Set next value to divide
        
        return result
