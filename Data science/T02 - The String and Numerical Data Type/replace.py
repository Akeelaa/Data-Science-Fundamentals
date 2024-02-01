#saving the sentence as a single string
original_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#replacing the "!" with blank space
edited_sentence = original_sentence.replace("!"," " )

print("edited Sentence:", edited_sentence)

#convert the sentence to upper case
upercase_sentence = edited_sentence.upper()

#Print the uppercase sentence
print("Uppercase sentence:", upercase_sentence)
      
#Print sentence in reverse
reverse_sentence = edited_sentence[::-1]
print("Reverse Sentence:", reverse_sentence)

         