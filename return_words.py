"""
Given a dictionary that maps a word to the frequency count (i.e., number of times the word occurs in a sentence),
write a function to return the total number of words in the sentence.

For example, if the sentence is "all is well that ends well",
then the dictionary will contain {"all":1, "is":1, "well":2, "that":1, "ends":1}.
Your function should count the total number of words in that dictionary (including duplicates).
For this example, your function should return 6.
"""

def count_total_words(word_freq):
    total = 0
    for i in word_freq:
        total += word_freq[i]

    return total