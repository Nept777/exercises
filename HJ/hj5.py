if __name__ == '__main__':
    s = input()
    s = s[2:]
    s_ = s[::-1]
    t=1
    result = 0
    dict = {    '0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15
                }
    for i in s_:
        get = dict.get(i)
        result = result + get * t
        t = t * 16
    print(result)
