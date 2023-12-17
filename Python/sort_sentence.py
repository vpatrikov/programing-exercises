def order(sentence):
    sentence = sentence.split()
    dictSentence = {}
    for word in sentence:
        for char in word:
            if char.isdigit():
               dictSentence[int(char)] = word
    sentence.clear()

    for i in range(1, (len(dictSentence) + 1)):
        sentence.append(dictSentence[i])

    return ' '.join(sentence)



print(order("is2 Thi1s T4est 3a"))