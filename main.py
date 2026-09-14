from file_reader import read_file
from analyzer import count_words
from analyzer import total_words
from analyzer import unique_words
from analyzer import Top3_words
from analyzer import average_words
from datetime import datetime
now = datetime.now()
text=read_file("text_analyzer/data/test.txt")
if text is None:
    print("文件不存在")
    raise SystemExit(1)
if total_words(text)==0:
    print("没有可分析的内容，已退出")
    raise SystemExit(1)
result=count_words(text)
# result=sorted(result.items(),key=lambda x:x[1],reverse=True)
print("====== Text Analysis Report ========================================")
# print(result)
print("total words:",total_words(text))
print("unique words:",unique_words(text))
Top3_words(text)
average_words(text)
print(now.strftime("%Y-%m-%d %H:%M"))
print("====================================================================")
