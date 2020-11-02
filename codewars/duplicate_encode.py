def duplicate_encode(word):
    word = word.lower()
    string = ''
    for letter in word:
        if word.count(letter.lower()) > 1:
            string += ')'
        else:
            string += '('
    return string
