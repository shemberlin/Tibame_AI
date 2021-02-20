import pymysql
import os
import prettytable as pt

passwd=input("請輸入資料庫root密碼:")
port=input("請輸入資料庫Port:")
if port=="":
    port="3306"

link=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="python_ai",
    charset="utf8",
    port=int(port)
)
os.system("cls")
db=link.cursor()
db.execute("SELECT * FROM `member`")
# for i in db.description:
    # print(i[0])
i=-1
while i!="0":
    if i=="1":
        db.execute("SELECT * FROM `member`")

        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址"])
        t.align="l"
        for d in data:
            t.add_row([d[0],d[1],d[2],d[3]]) 
            # print(d[0],d[1],d[2],d[3])
        print(t)
    if i=="2":
        os.system("cls")
        p={
            "a":input("請輸入會員姓名:" ),
            "b":input("請輸入會員生日:" ),
            "c":input("請輸入會員地址:" )
        }
        # db.execute("INSERT INTO member (name, birthday, address) VALUES("林鉉博","1994-01-22","台北市")")

        db.execute(
            "INSERT INTO `member`(`name`, `birthday`, `address`)"+
        "VALUES(%(a)s,%(b)s,%(c)s)",p
        )
        link.commit()
        os.system("cls")
    if i=="3":
        os.system("cls")
        db.execute("SELECT * FROM `member`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址"])
        t.align="l"
        for d in data:
            t.add_row([d[0],d[1],d[2],d[3]]) 
        print(t)
        u={
             "a":input("請選擇你要修改的資料編號："),
             "b":input("請輸入會員姓名:" ),
             "c":input("請輸入會員生日:" ),
             "d":input("請輸入會員地址:" )
        }
        db.execute("UPDATE `member` SET `name`=%(b)s,`birthday`=%(c)s,`address`=%(d)s WHERE `id`=%(a)s",u) 
        link.commit()
        os.system("cls")

    if i=="4":    
        db.execute("SELECT * FROM `member`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址"])
        t.align="l"
        for d in data:
            t.add_row([d[0],d[1],d[2],d[3]]) 
        print(t)

        delid=input("請選擇你要刪除的資料編號：") 
        db.execute("DELETE FROM `member` WHERE `id`=%s",delid)
        link.commit() 
        os.system("cls")


# SELECT `member`.`id`,`member`.name,`tel`.`tel` FROM `member` INNER JOIN `tel` ON `member`.`id`=`tel`.`member_id`

    
    print("(0) 離開程式\n(1) 顯示會員列表\n(2) 新增會員資料\n(3) 更新會員資料\n(4) 刪除會員資料")
    i=input("指令:")
    os.system("cls")
link.close

    



