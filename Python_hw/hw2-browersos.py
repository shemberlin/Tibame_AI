import os, sys

try:
    os.system("start "+sys.argv[1])
except:
    print("請輸入網址!")