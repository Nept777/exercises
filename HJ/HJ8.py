from typing import List

if __name__ == '__main__':
    n = int(input())
    dict = {}
    for i in range(0, n):
        s = input()
        splited: list[str] = s.split(" ")
        int0 = int(splited[0])
        int1 = int(splited[1])
        if int0 not in dict.keys():
            dict[int0] = int1
        else:
            dict[int0] = dict.get(int0) + int1

    dict = sorted(dict.items())
    for i in dict:
        print(str(i[0]) + " " + str(i[1]))
