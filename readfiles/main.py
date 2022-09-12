from datetime import datetime


def io_tools(read_filepath, write_filepath, mode):
    # mode:
    #   1 - read from txt and write to txt
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
    rangeOver = input("重复几次：")
    for i in range(0, int(rangeOver)):
        filename = f"G:/pythontest/{date}_{i}.txt"
        io_tools(r'G:\pythontest\test1.txt', filename, 1)


print(datetime.now())
main()
print(datetime.now())
