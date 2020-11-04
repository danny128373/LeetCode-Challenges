def rot13(message):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alpha_upper = list('abcdefghijklmnopqrstuvwxyz'.upper())
    new_message = ''
    for letter in list(message):
        if not letter.isalpha():
            new_message += ' '
            continue
        if letter.isupper():
            index = alpha_upper.index(letter)
        else:
            index = alphabet.index(letter)
        if letter.isupper() and index < 13:
            new_message += alpha_upper[index + 13]
        elif letter.isupper() and index >= 13:
            new_message += alpha_upper[index % 13]
        elif index < 13:
            new_message += alphabet[index + 13]
        else:
            new_message += alphabet[index % 13]
    return new_message


print(rot13("test"))
print(rot13("Test"))
