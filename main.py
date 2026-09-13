from file_reader import read_file
from analyzer import count_words
from analyzer import total_words
from analyzer import unique_words
from analyzer import Top3_words
text=read_file("data/test.txt")
# print(text)
result=count_words(text)
# result=sorted(result.items(),key=lambda x:x[1],reverse=True)
print("====== Text Analysis Report ========================================")
print(result)
print("total words:",total_words(text))
print("unique words:",unique_words(text))
print("top3 words",Top3_words(text))
print("====================================================================")
