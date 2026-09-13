from file_reader import read_file
from analyzer import count_words
text=read_file("data/test.txt")
# print(text)
result=count_words(text)
# result=sorted(result.items(),key=lambda x:x[1],reverse=True)
print(result)
