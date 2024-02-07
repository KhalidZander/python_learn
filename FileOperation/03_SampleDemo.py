with open("FileTest.txt","r",encoding="utf-8") as read_file:
    with open("FileTest_Back.txt","w",encoding="utf-8") as backup_file:
        count =0
        for line in read_file:
            if line.__contains__("real"):
                backup_file.write(line)
                count +=1
print(f"Backup Finish.Total Count: {count}")