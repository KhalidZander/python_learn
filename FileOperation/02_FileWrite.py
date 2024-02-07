import time

# 追加将w改为a即可
f = open("FileTest.txt","a",encoding="utf-8");

count =0

while count <10:
    time.sleep(1)
    f.write(f"{time.time()}\n")
    f.flush
    count +=1
    print(time.time());
f.close()