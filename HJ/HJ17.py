import re

if __name__ == '__main__':
    s = input()
    coord = (0,0)
    for i in s.split(";"):
        if re.match(r'^[ADWS][0-9]([0-9])?$', i) is not None:
            num = int(re.search(r'[0-9]+', i).group())
            if i[0] =='A':
                coord = (coord[0]-num, coord[1])
            elif i[0] =='W':
                coord = (coord[0], coord[1]+num)
            elif i[0] =='S':
                coord = (coord[0], coord[1]-num)
            elif i[0] =='D':
                coord = (coord[0]+num, coord[1])

    print(str(coord[0])+","+str(coord[1]))



