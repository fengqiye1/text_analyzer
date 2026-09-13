def count_words(txt):
    words = txt.replace(".", "").split()
    result={}
    for word in words:
        if(word in result):
            result[word]+=1
        else:
            result[word]=1
    return result

def total_words(txt):
    words = txt.replace(".", "").split()
    return len(words)
def unique_words(txt):
    words = txt.replace(".", "").split()
    return len(set(words))
def Top3_words(txt):
    words = count_words(txt)
    result_list=list(words.items())

    result_list.sort(key=lambda x:x[1],reverse=True)

    return [result_list[0][0],result_list[1][0],result_list[2][0]]
