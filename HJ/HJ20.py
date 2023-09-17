import re
import sys


def zichuanchongfu(s):
    # 不能有长度大于2的包含公共元素的子串重复
    list = []
    for i in range(3, len(s)):
        for j in range(0, len(s) - i + 1):
            # print(s[j:j + i])
            t = s[j:j + i]
            if t not in list:
                list.append(t)
            else:
                return False
    return True


def shumuzhonglei(s):
    cnt = 0
    if re.match(r'^[\S]{8,100}$', s) is not None:
        if re.search(r'[A-Z]', s) is not None:
            cnt += 1
        if re.search(r'[a-z]', s) is not None:
            cnt += 1
        if re.search(r'[0-9]', s) is not None:
            cnt += 1
        if re.search(r'[^(A-Za-z0-9\s)]', s) is not None:
            cnt += 1
        if cnt > 2:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':

    s = input()

    if zichuanchongfu(s) and shumuzhonglei(s):
        print("OK")
    else:
        print("NG")
