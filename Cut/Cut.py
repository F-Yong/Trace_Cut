import xdrlib ,sys
import xlrd
import xlwt
import time
import datetime
import os

Path = "./000000_0.txt"
P1 = "./1.txt"
P2 = "./2.txt"
P3 = "./3.txt"

# 主函数
def main():
    Index = 0
    f1 = open(P1, 'w')
    f2 = open(P2, 'w')
    f3 = open(P3, 'w')
   
    with open(Path) as f:
        lines = f.readlines()
        for line in lines:
            Index += 1;
            if(Index < 1000000):
                f1.writelines(line)
            elif(Index < 2000000):
                f2.writelines(line)
            else:
                f3.writelines(line)
    f1.close()
    f2.close()
    f3.close()
    
    
if __name__=="__main__":
    main()
