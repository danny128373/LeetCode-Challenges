from collections import Counter


# Times out but passes all tests
def scramble(s1, s2):
    s1 = list(s1)
    for letter in s2:
        if letter in s1:
            s1.remove(letter)
        else:
            return False
    return True


# slightly more efficient
def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0
