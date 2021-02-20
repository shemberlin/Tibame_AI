import os
import codecs

cmd="-1"
while cmd!="0":
    os.system("cls")
    count=0
    data=[]
    path=os.listdir("./")
    if cmd=="1":
        for a in path:
            if os.path.isfile(a):
                data.append(a)
                print(count,data[count]) 
                count+=1
        print("")       
    elif cmd=="2":
        for b in path:
            if os.path.isdir(b):
                data.append(b)
                print(count,data[count])
                count+=1
        print("")
    elif cmd=="3":
        for c in path:
            if os.path.isfile(c):
                data.append(c)
                print(count,data[count])
                count+=1
        print("")
        idx=int(input("請輸入檔案索引:"))
        with codecs.open(data[idx],"r","utf8") as f:
            os.system("cls")
            print("================檔案開始================")
            print(f.read())
            print("================檔案結束================")
    elif cmd=="4":
        for d in path:
            if os.path.isfile(d):
                data.append(d)
                print(count,data[count])
                count+=1
        print("")
        idx=int(input("請輸入檔案索引:"))
        os.remove(data[idx])
        os.system("cls")
    elif cmd=="5":
        for d in path:
            if os.path.isfile(d):
                data.append(d)
                print(count,data[count])
                count+=1
        print("")        
        idx=int(input("請輸入檔案索引:"))
        os.startfile(data[idx])
        os.system("cls")
        print("")
    elif cmd=="6":
        for e in path:
            if os.path.isdir(e):
                data.append(e)
                print(count,data[count])
                count+=1
        print("")
        idx=int(input("請輸入資料夾索引:"))
        os.chdir(data[idx])
        os.system("cls")
    elif cmd=="7":
        for f in path:
            if os.path.isdir(f):
                data.append(f)
                print(count,data[count])
                count+=1
        print("")
        idx=int(input("請輸入資料夾索引:"))
        os.rmdir(data[idx])
        os.system("cls")
    elif cmd=="8":
        os.chdir("..")
        os.system("cls")              
    print("工作路徑:",os.getcwd())
    print("\t(0) 離開程式\n\t(1) 列出檔案\n\t(2) 列出資料夾\n\t(3) 顯示檔案內容\n\t(4) 刪除檔案\n\t(5) 執行檔案\n\t(6) 進入資料夾\n\t(7) 刪除資料夾\n\t(8) 回上層資料夾")
    cmd=input("操作:")
    os.system("cls")