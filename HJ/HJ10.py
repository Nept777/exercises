if __name__ == '__main__':
    s = input()
    n = []
    for i in s:
        if i not in n :
            n.append(i)
    print(len(n))
