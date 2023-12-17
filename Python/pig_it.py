def pig_it(text):
    listWords = text.split(' ')

    punctioation = ['!', '.', ',', '?']
    temp = []
    result = []
    for word in listWords:
        if word in punctioation:
            result.append(word)
            break
        else:   
            temp = list(word)
            temp.append(temp[0])
            temp.remove(temp[0])
            temp.append ('a')
            temp.append('y')
            word = ''.join(temp)
            result.append(word)
    
    return ' '.join(result)