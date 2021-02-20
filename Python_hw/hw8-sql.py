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
    os.system("cls")
    if i=="1":
        os.system("cls") 
        db.execute("SELECT `m`.`id`, `m`.`name`, `m`.`birthday`,`m`.`address`, `t`.`tel` FROM `member` AS `m` LEFT JOIN `tel` AS `t` ON `m`.`id`=`t`.`member_id`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址","電話"])
        t.align="l"
        tmpid=[]
        for d in data:
            dlist=list(d)
            if tmpid==dlist[0]:
                t.add_row(["","","","",dlist[4]])
            else:
                t.add_row([dlist[0],dlist[1],dlist[2],dlist[3],dlist[4]])    
            tmpid=dlist[0]
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
        os.system("cls") 
        db.execute("SELECT `m`.`id`, `m`.`name`, `m`.`birthday`,`m`.`address`, `t`.`tel` FROM `member` AS `m` LEFT JOIN `tel` AS `t` ON `m`.`id`=`t`.`member_id`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址","電話"])
        t.align="l"
        tmpid=[]
        for d in data:
            dlist=list(d)
            if tmpid==dlist[0]:
                t.add_row(["","","","",dlist[4]])
            else:
                t.add_row([dlist[0],dlist[1],dlist[2],dlist[3],dlist[4]])    
            tmpid=dlist[0]
        print(t)         
        delid=input("請選擇你要刪除的資料編號：")
        db.execute("DELETE FROM `member` WHERE `id`=%s",delid)
        link.commit() 
        os.system("cls")
    if i=="5":
        os.system("cls") 
        db.execute("SELECT `m`.`id`, `m`.`name`, `m`.`birthday`,`m`.`address`, `t`.`tel` FROM `member` AS `m` LEFT JOIN `tel` AS `t` ON `m`.`id`=`t`.`member_id`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址","電話"])
        t.align="l"
        tmpid=[]
        for d in data:
            dlist=list(d)
            if tmpid==dlist[0]:
                t.add_row(["","","","",dlist[4]])
            else:
                t.add_row([dlist[0],dlist[1],dlist[2],dlist[3],dlist[4]])    
            tmpid=dlist[0]
        print(t)
        u={
             "a":input("請選擇要添加電話的會員編號："),
             "b":input("請輸入電話：" )
        }
        db.execute("INSERT INTO `tel`(`member_id`,`tel`) VALUES(%(a)s,%(b)s)",u)
        link.commit()
        os.system("cls")
    if i=="6":
        db.execute("SELECT `m`.`id`, `m`.`name`, `m`.`birthday`,`m`.`address`, `t`.`tel` FROM `member` AS `m` LEFT JOIN `tel` AS `t` ON `m`.`id`=`t`.`member_id`")
        data=db.fetchall()
        t=pt.PrettyTable(["編號","姓名","生日","地址","電話"])
        t.align="l"
        tmpid=[]
        for d in data:
            dlist=list(d)
            if tmpid==dlist[0]:
                t.add_row(["","","","",dlist[4]])
            else:
                t.add_row([dlist[0],dlist[1],dlist[2],dlist[3],dlist[4]])    
            tmpid=dlist[0]
        print(t)
        db.execute("SELECT `id`,`tel` FROM `tel` WHERE `member_id`=%s ORDER BY `id` ASC",[input("請選擇要刪除電話的會員編號：")])
        t=pt.PrettyTable(["編號","電話"])
        for d in db.fetchall():
            t.add_row([d[0],d[1]])
        print(t)
        db.execute("DELETE FROM `tel` WHERE `id`=%s",[input("請輸入要刪除的電話編號：")])
        link.commit()
        os.system("cls")              
# SELECT `member`.`id`,`member`.name,`tel`.`tel` FROM `member` INNER JOIN `tel` ON `member`.`id`=`tel`.`member_id`
    print("(0) 離開程式\n(1) 顯示會員列表\n(2) 新增會員資料\n(3) 更新會員資料\n(4) 刪除會員資料\n(5) 新增會員的電話\n(6) 刪除會員的電話")
    i=input("指令:")
    os.system("cls")
link.close
    

    



