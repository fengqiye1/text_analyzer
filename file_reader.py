def read_file(path):
    try:
        with open(path,"r",encoding='utf-8') as f:
           return f.read()
    except FileNotFoundError:
        print("文件不存在")
        return ""
