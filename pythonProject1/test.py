from datetime import datetime

def io_tools(read_filepath, write_filepath, mode):
    if mode == 1:
        file = open(read_filepath, "rb+")
        file_to_write = open(write_filepath, "wb+")
        strlines = file.read()
        file_to_write.write(strlines)
        file_to_write.close()
        file.close()

def main():
    now = datetime.now()
    date = now.strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"G:/pythontest/{date}.txt"
    for int in range(0,3):
        filename = f"G:/pythontest/{date}_{int}.txt"
        io_tools(r'G:\pythontest\test1.txt', filename, 1)

#todo 输入输入输出文件名和mode
#todo 输入循环次数


main()