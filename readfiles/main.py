from datetime import datetime
import time
import xlwings


def io_tools(read_filepath, write_filepath, mode):
    # mode:
    #   1 - read from txt and write to txt
    #   2 - read from excel by some rule and write to dict[]
    if mode == 1:
        file = open(read_filepath, "rb+")
        file_to_write = open(write_filepath, "wb+")
        strlines = file.read()
        file_to_write.write(strlines)
        file_to_write.close()
        file.close()
    elif mode == 2:
        app = xlwings.App(visible=True, add_book=False)
        file = xlwings.Book(read_filepath)
        sheet = file.sheets['Sheet1']
        if sheet.range('A2').value != 'idx':
            print('Config ERROR')
            return
        maplist = {}

        rowcnt = sheet.range('A1').current_region.columns[0].rows.count
        if (rowcnt - 2) % 8 != 0:
            print('Config ERROR')
            return
        idxcnt = int((rowcnt - 2) / 8)
        for x in range(idxcnt):
            # print(sheet.range(f'B{3+x*8}:P{8+x*8}').value)

            # 8 = 宽度 MAP_COL
            # B{}:P{}可以用tuple
            maplist[x+1] = sheet.range(f'B{3+x*8}:P{10+x*8}').value

        # print(maplist)
        file.close()
        app.quit()


def main():
    now = datetime.now()
    date = now.strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"G:/pythontest/{date}.txt"
    # rangeOver = input("重复几次：")
    # for i in range(0, int(rangeOver)):
    #    filename = f"G:/pythontest/{date}_{i}.txt"
    #    io_tools(r'G:\pythontest\test1.txt', filename, 1)
    io_tools(r'G:\pythontest\test2.xls', filename, 2)

print(datetime.now())
main()
print(datetime.now())


