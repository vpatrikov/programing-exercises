def spin_words(sentence):
    sentence_lst = sentence.split(' ')

    for i in range(len(sentence_lst)):
        if len(sentence_lst[i]) >= 5:
            sentence_lst[i] = sentence_lst[i][::-1]

    return ' '.join(sentence_lst)