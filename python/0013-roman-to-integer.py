# Objective: Convert from Roman numerals to Arabic numerals

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Hash table
        roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50,
                  "C" : 100, "D" : 500, "M" : 1000}
        
        result = 0 # Placeholder value for the conversion
        
        # For each symbol, subtract values smaller than next one
        # Add symbols bigger or equal in value to next
        try:
            for i in range(len(s)):
            
                if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                    result -= roman[s[i]]
                
                else:
                    result += roman[s[i]]

            print("Good job. Your answer is: ")
            return result
        
        except: # Error message for invalid input. Suggested by my girlfriend.
            print("Uh oh, seems like something went wrong. \
Make sure that your input is a valid Roman numeral. You've got this, honey.")
