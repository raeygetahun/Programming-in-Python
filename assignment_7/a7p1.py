def longest_word(lst):
    longest = ""
    for word in lst:
        if len(word) > len(longest):
            longest = word
    return longest

input_string = input("Enter a string of words: ")

word_list = input_string.split()

print(longest_word(word_list))