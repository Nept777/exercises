
if __name__ == '__main__':
    ins = input()
    lenth = len(ins)
    i = 0
    while i < lenth:
        # if (i+8)>lenth:
        #     result = ins[i:lenth-1]+""
        ins_t = ins[i:i+8]
        if (i + 8) > lenth:
            for n in range(0,(i+8) - lenth):
                ins_t = ins_t+"0"
        print(ins_t)
        i=i+8





