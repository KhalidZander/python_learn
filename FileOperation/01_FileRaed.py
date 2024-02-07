# f = open("test.txt", "r", encoding="utf-8")
# 第一次读取
#print(f.read(3))
# 第二次读取 从上次读取的位置开始读取
#print(f.read(3))

#lines = f.readlines()
#print(f"Type:{type(lines)} Content{lines}")

#判断有多少个Hello

# count = f.read().count("Hello")

with open("test.txt","r",encoding="utf-8") as f:
    count = 0
    for line in f:
        words = line.strip().split(" ")
        for word in words:
            if word =="Hello":
                count+=1
                
    print(f"Hello出现的次数:{count}")
