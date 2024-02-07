def print_file_info(path):
    f = None
    try:
        f = open(path,"r",encoding="utf-8")
        contend = f.read()
        print("文件内容如下：\n"+contend)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close

def append_to_file(path:str,data):
    f =  open(path,"a",encoding="utf-8")
    try:
        f.write(data+"\n")
        print("文件添加完成")
    except Exception as e:
        print(e)
    finally:
        f.close
