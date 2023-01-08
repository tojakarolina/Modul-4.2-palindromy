def if_palindrom (word):
    word_2 = ""
    for letter in range( len(word) -1, -1, -1):
            word_2 += word[letter]
    if word_2 == word:
            return True
    else:
            return False

palindrom = if_palindrom("kajak")
print(palindrom)
    