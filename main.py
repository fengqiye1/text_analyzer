from file_reader import read_file
from analyzer import count_words
text=read_file("data/test.txt")
# print(text)
result=count_words(text)
print(result)
