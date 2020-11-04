import re
import collections


def top_3_words(text):
    text = text.split()
    text_wout_punc = []
    list_of_tup = []
    top3 = []
    answer = []
    for word in text:
        if word.isalpha():
            text_wout_punc.append(word.lower())
        else:
            match = re.sub(r'[^\w\s]', '', word)
            text_wout_punc.append(match[0].lower())
    text_wout_punc = collections.Counter(text_wout_punc)
    for k, v in text_wout_punc.items():
        list_of_tup.append((v, k))
    list_of_tup.sort(key=lambda tup: tup[0])
    top3.append(list_of_tup[-1])
    top3.append(list_of_tup[-2])
    top3.append(list_of_tup[-3])
    for tup in top3:
        answer.append(tup[1])
    return answer


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
