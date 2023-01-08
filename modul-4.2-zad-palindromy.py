def if_palindrom (word):
    word_2 = ""
    for letter in range( len(word) -1, -1, -1):
            word_2 += word[letter]

    return word_2

palindrom = if_palindrom("kocyk")
print(palindrom)
    