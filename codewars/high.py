def high(x):
    x = x.split()
    alphabet_dict = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    highest_score = 0
    highest_score_word = ''
    for letter in range(len(alphabet)):
        alphabet_dict[alphabet[letter]] = letter + 1
    for word in x:
        sum = 0
        for letter in word:
            sum += alphabet_dict[letter]
        if sum > highest_score:
            highest_score_word = word
            highest_score = sum
    return highest_score_word


print(high('what time are we climbing up the volcano'))
