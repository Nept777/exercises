import sys
import math

if __name__ == "__main__":
    n: int = int(input())

    for i in range(2,int(math.sqrt(n))+1):
        while (n % i == 0):
            print(int(i),end=" ")
            n = n/i
    if n > 1:print(int(n),end=" ")
