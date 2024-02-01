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

# this will test the functions
print(alternate_case("Hello World"))  # Outputs: HeLlO WoRlD
print(alternate_word_case("I am learning to code"))  # Outputs: i AM learning TO code


