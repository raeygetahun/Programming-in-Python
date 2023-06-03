def substitute_vowels(str, ch):
    vowels=['a','e','i','o','u']
    output=''
    for char in str:
        if char.lower() in vowels:
            output+=ch
        else:
            output+=char
            
    return output

s = "This is a sentence"
print(s)
n = substitute_vowels(s, 'o')
print(n)
