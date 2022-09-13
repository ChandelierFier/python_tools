from datetime import datetime
import time


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
    #rangeOver = input("重复几次：")
    #for i in range(0, int(rangeOver)):
    t_end = time.time() + 1
    i = 0
    while time.time() < t_end:
            filename = f"F:/pythontest/{date}_{i}.txt"
            io_tools(r'F:\ForTest\temp1.txt', filename, 1)
            i = i+1




main()


