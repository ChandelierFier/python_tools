import random
from datetime import datetime
import xlwings


def getMapFrame(read_filepath):
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
        maplist[x + 1] = sheet.range(f'B{3 + x * 8}:P{10 + x * 8}').value

    file.close()
    app.quit()
    return maplist


def output_SolvedMap(output_filepath):
    # TODO
    return True


class LinkGame(object):
    MAP_ROW = 8
    MAP_COLUMN = 15
    ELEMENT_TYPE = 4

    def __init__(self, mapframe):
        self.mapframe = mapframe

    def isValid_Frame(self):
        if len(self.mapframe) != LinkGame.MAP_COLUMN or len(self.mapframe[0]) != LinkGame.MAP_ROW:
            print('mapframe ERROR')
            return False
        return True

    def totalCell(self):
        counts = 0
        for v in range(len(self.mapframe)):
            for k in range(len(self.mapframe[v])):
                if self.mapframe[v][k] is not None:
                    counts += 1
        return counts

    def isValid_ElementCnt(self):
        if (self.totalCell() / self.ELEMENT_TYPE) % 2 != 0:
            print('ElementCnt ERROR')
            return False
        return True

    def drawMap(self):
        defaultstr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcd'
        if not (self.isValid_Frame or self.isValid_ElementCnt):
            return False
        half_map = []
        temp_map = []
        element_type = []
        for i in range(LinkGame.ELEMENT_TYPE):
            element_type.append(defaultstr[i])
        for v in range(int(self.totalCell() / 2)):
            half_map.append(random.choice(element_type))
        temp_map = half_map[:]
        position = random.choice(range(int(self.totalCell() / 2)))
        temp_map = half_map[:position] + half_map + half_map[position:]
        # print(temp_map)
        it = iter(temp_map)
        for j in range(len(self.mapframe)):
            for k in range(len(self.mapframe[j])):
                if self.mapframe[j][k] is not None:
                    self.mapframe[j][k] = next(it)      # next()好像有概率会爆炸
        print("Map after insert elements: \n", self.mapframe)
        return True

    def getRandomStarter(self):
        random_starter_x = random.choice(range(LinkGame.MAP_ROW))
        random_starter_y = random.choice(range(LinkGame.MAP_COLUMN))
        return self.mapframe[random_starter_y][random_starter_x]

    # 解图
    def isValid_Map(self):
        #solved_map = [[None] * LinkGame.MAP_ROW] * LinkGame.MAP_COLUMN
        solved_map = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        ]
        while True:
            random_starter_x = random.choice(range(LinkGame.MAP_COLUMN))
            random_starter_y = random.choice(range(LinkGame.MAP_ROW))
            if self.mapframe[random_starter_y][random_starter_x] is not None:
                starter_x = random_starter_x
                starter_y = random_starter_y
                break
        print("Start point: ", starter_x, starter_y)
        for j in range(len(self.mapframe)):
            for k in range(len(self.mapframe[j])):
                if self.havePath(self.mapframe[starter_y][starter_x], self.mapframe[j][k]):
                    solved_map[starter_y][starter_x] = self.mapframe[starter_y][starter_x]
                    solved_map[j][k] = self.mapframe[j][k]
                    break
                if self.havePath_Type1(self.mapframe[starter_y][starter_x], self.mapframe[j][k]):
                    solved_map[starter_y][starter_x] = self.mapframe[starter_y][starter_x]
                    solved_map[j][k] = self.mapframe[j][k]
                    break
                if self.havePath_Type2(self.mapframe[starter_y][starter_x], self.mapframe[j][k]):
                    solved_map[starter_y][starter_x] = self.mapframe[starter_y][starter_x]
                    solved_map[j][k] = self.mapframe[j][k]
                    break
        print("Solved Map", solved_map)
        return True

    # 直连
    def havePath(self, point1, point2):
        # TODO
        return True

    # 转一个角
    def havePath_Type1(self, point1, point2):
        # TODO
        return True

    # 转两个角
    def havePath_Type2(self, point1, point2):
        # TODO
        return True

def main():
    now = datetime.now()
    date = now.strftime("%Y_%m_%d_%H_%M_%S")
    filename = r'G:\pythontest\test2.xls'
    maplist = getMapFrame(filename)
    print("MapFrame read from excel: \n", maplist[1])
    game = LinkGame(maplist[1])
    LinkGame.drawMap(game)
    LinkGame.isValid_Map(game)



    # for v in range(len(maplist)):
    #    game = LinkGame(maplist[v+1])
    #    LinkGame.drawMap(game)



print(datetime.now())
main()
print(datetime.now())
