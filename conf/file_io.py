print("Practice working with file input and output")
def write_file(file_name,file_content):
    with open(file_name,"w") as file:
        file.write(file_content+"." +"\n")
def append_file(file_name,file_content):
    with open(file_name,"a") as file:
        file.write(file_content+"." +"\n")
def read_file(file_name):
    with open(file_name,encoding="utf-8") as file:
        for line in file:
            print(line)
write=write_file("write.txt","Test if the function is working")
append=append_file("write.txt","Add this text also")
append=append_file("write.txt","Check if text is moving to new line.")
read=read_file("write.txt")
def read_again(file_name):
    with open(file_name,encoding="utf-8") as file:
        print(file.read())
read_again=read_again("write.txt")
def again_read(file_name):
    file=open(file_name,encoding="utf-8")
    print(file.read())
again_read=again_read("write.txt")