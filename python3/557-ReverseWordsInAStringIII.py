# Objective: Given a phrase, return the phrase with each individual
# word reversed.

class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split() # split string into list of words
        reverse_words = ""

        for i in word_list:
            for j in reversed(i): # reverse individual words
                reverse_words += j
            
            reverse_words += " " # add space after each word
        
        return reverse_words[:-1]
