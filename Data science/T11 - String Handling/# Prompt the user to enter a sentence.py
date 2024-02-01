# This function is to alternate the case of characters in a string
# Input: s - the input string
# Output: a new string with characters alternating between uppercase and lowercase
def alternate_case(s):
    return "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))

# This function is to alternate the case of words in a string
# Input: s - the input string
# Output: a new string with words alternating between uppercase and lowercase
def alternate_word_case(s):
    return " ".join(w.upper() if i % 2 != 0 else w.lower() for i, w in enumerate(s.split()))

# Get input from the user
sentence = input("Please enter a sentence: ")

# Test the functions with user input
print("Alternate Case:", alternate_case(sentence))
print("Alternate Word Case:", alternate_word_case(sentence))
