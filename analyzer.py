def count_words(txt):
    words = txt.replace(".", "").split()
    result={}
    for word in words:
        if(word in result):
            result[word]+=1
        else:
            result[word]=1
    return result

