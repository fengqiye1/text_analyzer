def read_file(path):
    with open(path,"r",encoding='utf-8') as f:
        content=f.read()
    return content