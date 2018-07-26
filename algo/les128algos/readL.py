import sys
from sys import stdin
import fileinput

def readint():
    return int(stdin.readline())

def readarray(typ):
    return list(map(typ, stdin.readline().split()))



if __name__ == "__main__":
    n = readarray(int)
    print(n) 

print("printing stuff")

print('Hello world\n')
repr('Hello world\n')
