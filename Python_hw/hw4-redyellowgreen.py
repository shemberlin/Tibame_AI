import colorama
import time
import os

os.system("cls")
colorama.init(True)
while True:
    for i in range(1,6):
        print(colorama.Back.RED+"  ")
        print(i)
        time.sleep(1)
        os.system("cls")
        
    for i in range(6,7):
        print("   "+colorama.Back.YELLOW+"  ")
        print(i)
        time.sleep(1)
        os.system("cls")

    for i in range(7,11):
        print("      "+colorama.Back.GREEN+"  ")
        print(i%10)
        time.sleep(1)
        os.system("cls")
