import re
def count_words(txt):
    words=re.sub(r"[^a-zA-Z0-9]", " ", txt).split()
    result={}
    for word in words:
        if(word in result):
            result[word]+=1
        else:
            result[word]=1
    return result

def total_words(txt):
    words=re.sub(r"[^a-zA-Z0-9]", " ", txt).split()
    return len(words)
def unique_words(txt):
    words=re.sub(r"[^a-zA-Z0-9]", " ", txt).split()
    return len(set(words))
def Top3_words(txt):
    if(unique_words(txt)<3):
        print("unique words <3")
        return
    words = count_words(txt)
    result_list=list(words.items())

    result_list.sort(key=lambda x:x[1],reverse=True)
    print("top3 words:")
    print(f"{result_list[0][0]}: {result_list[0][1]}次\n{result_list[1][0]}: {result_list[1][1]}次\n{result_list[2][0]}: {result_list[2][1]}次")
def average_words(txt):
    words=re.sub(r"[^a-zA-Z0-9]", " ", txt).split()
    num=total_words(txt)
    sum_len=0
    for word in words:
        sum_len+=len(word)
    print("averagelenth:",f"{sum_len/num:.1f}")