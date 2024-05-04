import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='Lumia520',database='sgt1')

if con.is_connected():
    print("Connection established....")

c = con.cursor()

def Create_Account():
    ac_n = int(input("Enter Account Number : "))
    n = input("Enter Name : ")
    p = input("Enter Password : ")
    ac_b = int(input("Enter Amount : "))
    ac_t = input("Enter Account Type (C/S): ")
    s = "insert into bank(ac_n,name,password,ac_b,ac_t) values('%d','%s','%s','%d','%s')"%(ac_n,n,p,ac_b,ac_t)
    r = c.execute(s)
    if(r!=0):
        print("Record Insert : ")
    con.commit()

def show_Record():
    qry = "select * from bank"
    c.execute(qry)

    for data in c.fetchall():
        print(data[0], data[1],data[2],data[3],data[4])
    con.commit()

def Balance_Enc():
    ac_n = int(input("Enter Account Number : "))
    s= "select *from bank where ac_n='%d'"%(ac_n)
    c.execute(s)
    for data in c.fetchall():
        print(data[0],data[1],data[2],data[3],data[4])
    con.commit()

def dep_Amount():
    ac =0
    ac_n= int(input("Enter Account Number : "))
    amount = int(input("Enter Amount : "))
    s = "select ac_b from bank where ac_n='%d'"%(ac_n)
    c.execute(s)
    for data in c.fetchall():
        ac = data[0]
    total_amount = ac+amount
    s1 = "update bank set ac_b='%d' where ac_n='%d'"%(total_amount,ac_n)
    r=c.execute(s1)
    if(r!=0):
        print("Record Update : ")
    else:
        print("Record Not Update")


    con.commit()


def Withdraw_Amount():
    ac = 0
    ac_n = int(input("Enter Account Number : "))
    amount = int(input("Enter Amount : "))
    s = "select ac_b from bank where ac_n='%d'" % (ac_n)
    c.execute(s)
    for data in c.fetchall():
        ac = data[0]
    total_amount = ac - amount
    s1 = "update bank set ac_b='%d' where ac_n='%d'" % (total_amount, ac_n)
    r = c.execute(s1)
    if (r != 0):
        print("Record Update : ",total_amount)
    else:
        print("Record Not Update")

    con.commit()


def Bank():
    print("BANK MANAGEMENT SYSTEM : ")
    print("Welcome IN SBI : ")
    while(True):
        op = int(input("Main Menu : \n1. Create New Account\n2. Show All Account\n3. Balance Enquery \n4. Deposit Amount \n5. Withdraw Amount \nSelect Your Option : \n"))
        if(op == 1):
            Create_Account()
        elif(op == 2):
            show_Record()
        elif(op == 3):
            Balance_Enc()
        elif(op == 4):
            dep_Amount()
        elif(op == 5):
            Withdraw_Amount()

        else:
            break

Bank()

