import mysql.connector as ms
import random as r
con=ms.connect(host='localhost', user='root', passwd='abc@123', database='job')
cur=con.cursor()

def start_company():
        print("**"*30)
        print(" "*15,"PROFESSIONAL NETEWORK SERVICES")
        print("**"*30)
        print("What do you want to do?")
        print("1.Add Company\n2.Modify Company\n3.Search Company\n4.Delete Company\n5.Exit")
        c2=int(input("Enter your choice: "))
        if c2==1:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            add_company()
            print()
        elif c2==2:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            modify_company()
            print()
        elif c2==3:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            search_company()
            print()
        elif c2==4:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            delete_company()
            print()
        elif c2==5:
            print()
            import Main as menu
            print("PROFESSIONAL NETWORK SERVICES")
            menu.main_menu()
            print()

def add_company():

    q="select cID from company"
    cur.execute(q)
    idl=cur.fetchall()
    while True:
        i=r.randint(10001,99999)
        if (i,) not in idl:
            ID=i
            break
        else:
            continue        
    print("Your new Company ID: ", ID)

    name=input("Enter Company Name: ").title()
    em=input("Enter Company Email: ")
    qual=input("Enter your required Qualification: ")
    jt=input("Enter the required Job Title: ").title()
    exp=int(input("Enter required Experience (in years): "))
    novac=int(input("Enter number of Vacancies: "))
    loc=input("Enter City Name: ").title()

    query="insert into company (cID,cname,cemail,qualification,cjobtitle,exp,vacancy,City)\
        values({},'{}','{}','{}','{}',{},{},'{}')".format(ID,name,em,qual,jt,exp,novac,loc)
    
    cur.execute(query)
    con.commit()
    print("Record Updated")

def modify_company():
    ID=int(input("Enter the Company ID to modify:"))
    query="select * from company where CID={}".format(ID)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>=1:
        for i in res:
            print("ID: ",i[0])
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Qualification: ',i[3])
            print('Job Title: ',i[4])
            print('Experience: ',i[5],'year(s)')
            print("Number of Vacancy: ",i[6])
            print('City: ',i[7])

            print("Do you want to modify?")
            ch=input("(Y/N): ")
            if ch in 'Yy':
                print("What do you want to modify? ")
                print("1. Name\n2. Email\n3. Qualification\n4. Job Title\n5. Experience\n6. Number of Vacancy\
                      \n7. City")
                ans=int(input("Enter your choice: "))
                if ans==1:
                    new=input("Enter new name: ")
                    q="update company set cname='{}' where CID={}".format(new,ID)
                elif ans==2:
                    new=input("Enter new Email: ")
                    q="update company set cEmail='{}' where CID={}".format(new,ID)
                elif ans==3:
                    new=input("Enter new Qualification: ")
                    q="update company set qualification='{}' where CID={}".format(new,ID)
                elif ans==4:
                    new=input("Enter new Job Title: ")
                    q="update company set cjobtitle='{}' where CID={}".format(new,ID)
                elif ans==5:
                    new=int(input("Enter new experience: "))
                    q="update company set experience={} where CID={}".format(new,ID)
                elif ans==6:
                    new=int(input("Enter new Number of Vacancy: "))
                    q="update company set vacancy={} where CID={}".format(new,ID)            
                elif  ans==7:
                    new=input("Enter new City: ")
                    q="update company set City='{}' where CID={}".format(new,ID)
                cur.execute(q)
                con.commit()
                print("Modification Completed")

            else:
                print("No Modification done")

    else:
        print("No Company found with",ID, "ID")

def delete_company():
    ID=int(input("Enter ID to be deleted: "))
    query="select * from company where CID={}".format(ID)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>=1:
        for i in res:
            print("ID: ",i[0])
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Qualification: ',i[3])
            print('Job Title: ',i[4])
            print('Experience: ',i[5],'year(s)')
            print("Number of Vacancy: ",i[6])
            print('City: ',i[7])           
             
            print("Do you want to delete?")
            ans=input("(Y/N): ")
            if ans in "Yy":
                q="delete from company where CID={}".format(ID)
                cur.execute(q)
                con.commit()
                print("Record Deleted")
            else:
                print("No Record Deleted")
    else:
        print("No record found with", ID,"ID")

def search_company():
    ID=int(input("Enter company ID to search: "))
    query="select * from company where CID={}".format(ID)
    cur.execute(query)
    data=cur.fetchall()
    if cur.rowcount>=1:
        for i in data:
            print("ID: ",i[0])
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Qualification: ',i[3])
            print('Job Title: ',i[4])
            print('Experience: ',i[5],'year(s)')
            print("Number of Vacancy: ",i[6])
            print('City: ',i[7])
    else:
        print("No company found with ID: ",ID)
