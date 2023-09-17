import re

if __name__ == '__main__':
    # 输入字符串
    str = input()

    str=list(str)

    # 冒泡
    for i in range(0, len(str) - 1):
        for j in range(0, len(str)-i-1):
            n=1
            flag = True
            # 是否是英文字母
            # 如果左值为非字母,直接跳过
            if re.match(r'[a-zA-Z]', str[j]) is None : continue
            # 如果右值为非字母,看右值下一个字符,以此类推直到看到字母或者句尾为止
            while re.match(r'[a-zA-Z]', str[j + n]) is None:
                if j+n == len(str)-i-1:
                    flag=False
                    break
                n+=1
            if not flag: break
            # 比较大小 把大的往后排
            if str[j].lower() > str[j+n].lower():
                str[j+n], str[j] = str[j], str[j+n]

            # print(str[j], end='')
        # print(str)

    print(''.join(str))