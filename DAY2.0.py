def get_word(sentence, n):
    if n>0:
        words = sentence.split()
        if n <= len(words) and n>0:
             return(words[n-1])
    else:
        return ""

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5))

print(get_word("This is lession about list", 4))