if __name__ == '__main__':
    line = input()
    reline = ""
    dirc = {}
    for s in line:
        if s in dirc.keys():
            dirc[s] += 1
        else:
            dirc[s] = 1
    for d in dirc.keys():
        if dirc[d] == min(dirc.values()):
            line = line.replace(d, '')

    print(line)