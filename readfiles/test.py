import copy


def main():
    list1 = [[None,None,None],[None,None,None]]

    list2 = [[0,1,0],[3,0,2]]
    for j in range(2):
        for k in range(3):
            if list2[j][k] > 0:
                print(j,k)
                list1[j][k] = list2[j][k]
                print(list1)
    print(list1)
    print(list2)
    return 0


main()