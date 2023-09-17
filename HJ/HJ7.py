if __name__ == '__main__':
    f = float(input())
    fint = f.__int__()
    fpoint = f - fint
    if fpoint < 0.5:
        print(fint)
    else:
        print(fint+1)


