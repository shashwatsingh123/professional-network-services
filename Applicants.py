import mysql.connector as ms
import datetime 
import random as r
con=ms.connect(host='localhost', user='root', passwd='abc@123', database='job')
cur=con.cursor()

def start_applicants():
    print("**"*30)
    print(" "*15,"PROFESSIONAL NETEWORK SERVICES")
    print("**"*30)

    print("What do you want to do?")
    print("1.Add Applicant\n2.Modify Applicant\n3.Search Applicant\n4.Delete Applicant\n5.Exit")
    c2=int(input("Enter your choice: "))
    if c2==1:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        add_applicant()
        print()
    elif c2==2:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        modify_applicant()
        print()
    elif c2==3:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        search_applicant()
        print()
    elif c2==4:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        delete_applicant()
        print()
    elif c2==5:
        import Main as menu
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        menu.main_menu()
        print()

def applied(apid,apname,coid,jt,loc):
    q="insert into applied (apid,apname,coid,jt,loc) values({},'{}',{},'{}','{}')".format(apid,apname,coid,jt,loc)
    cur.execute(q)
    con.commit()
    vac1="update company set vacancy=vacancy-1 where cid={}".format(coid)
    cur.execute(vac1)
    con.commit()

def add_applicant():

    q="select AID from applicants"
    cur.execute(q)
    idl=cur.fetchall()
    while True:
        i=r.randint(1001,9999)
        if (i,) not in idl:
            ID=i
            break
        else:
            continue
    print("Your new Applicant ID: ", ID)
    name=input("Enter Name: ").title()
    em=input("Enter Email: ")
    g=input("Enter Gender: ").upper()

    print("Enter Date of Application")
    dd=int(input("Enter the Date: "))
    mm=int(input("Enter the Month: "))
    yy=int(input("Enter the Year: "))
    date1=datetime.date(yy,mm,dd)
    date_str = date1.strftime('%Y-%m-%d')

    jt=input("Enter the Job Title: ").title()
    qual=input("Enter your Qualification: ")
    exp=int(input("Enter Experience (in years): "))
    emp=input("Enter 'Y' if already employed else, 'N': ").upper()
    #cs=input("Enter current Status (New/In Review/Rejected/Hired): ").upper()
    loc=input("Enter City Name: ").title()

    query="insert into applicants (AID,aname,email,gender,dateapplied,jobtitle,qualification,experience,empstatus,City)\
        values({},'{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(ID,name,em,g,date_str,jt,qual,exp,emp,loc)
    
    cur.execute(query)
    con.commit()
    print("Record Updated")

def modify_applicant():
    ID=int(input("Enter the Applicant ID to modify:"))
    query="select * from applicants where AID={}".format(ID)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>=1:
        for i in res:
            print("ID: ",i[0])
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Gender: ',i[3])
            print('Date Applied: ',i[4])
            print('Job Title: ',i[5])
            print("Qualification: ",i[6])
            print('Experience: ',i[7],'year(s)')
            print('Employment Status: ',i[8])
            print('Current Status: ',i[9])
            print('City: ',i[10])
            print()
            print("Do you want to modify?")
            ch=input("(Y/N): ")
            print()
            if ch in 'Yy':
                print("What do you want to modify? ")
                print("1. Name\n2. Email\n3. Gender\n4. Date Applied\n5. Job Title\n6. Qualification \n7. Experience\n8. Employment Status\
                       \n9. Current Status\n10. City")
                ans=int(input("Enter your choice: "))
                if ans==1:
                    new=input("Enter new name: ")
                    q="update applicants set Aname='{}' where AID={}".format(new,ID)
                
                elif ans==2:
                    new=input("Enter new Email: ")
                    q="update applicants set Email='{}' where AID={}".format(new,ID)
                
                elif ans==3:
                    new=int(input("Enter new Gender: "))
                    q="update applicants set Gender='{}' where AID={}".format(new,ID)
                
                elif ans==4:
                    print("Enter the new date: ")
                    yy=int(input("Enter the Year: "))
                    mm=int(input("Enter the Month: "))
                    dd=int(input("Enter the Date: "))
                    date1=datetime.date(yy,mm,dd)
                    new = date1.strftime('%Y-%m-%d')
                    q="update applicants set dateapplied='{}' where AID={}".format(new,ID)
                
                elif ans==5:
                    new=input("Enter new Job Title: ")
                    q="update applicants set jobtitle='{}' where AID={}".format(new,ID)
                
                elif ans==6:
                    new=input("Enter new Qualification: ")
                    q="update applicants set Qualification='{}' where AID={}".format(new,ID)
                
                elif ans==7:
                    new=int(input("Enter new experience: "))
                    q="update applicants set experience={} where AID={}".format(new,ID)
                
                elif ans==8:
                    new=input("Enter new Employment Status: ")
                    q="update applicants set empstatus='{}' where AID={}".format(new,ID)
                
                elif ans==9:
                    print("Enter new Current Status \n1.Hired\n2.In Review\n3.Rejected\n")
                    newstatus=int(input("Enter your choice: "))
                    if newstatus==2:
                        new="In Review"
                    elif newstatus==3:
                        new="Rejected"
                    elif newstatus==1:
                        while True:
                            cidd=int(input("Enter hiring company ID: "))
                            qu="select cID from company"
                            cur.execute(qu)
                            idl=cur.fetchall()
                            if (cidd,) in idl:
                                applied(i[0],i[1],cidd,i[5],i[10])
                                break
                            else:
                                print("Company ID doesn't exist!")
                                print("")
                                continue
                        new="Hired"
                    q="update applicants set cstatus='{}' where AID={}".format(new,ID)
                
                elif  ans==10:
                    new=input("Enter new City: ")
                    q="update applicants set City='{}' where AID={}".format(new,ID)
                
                cur.execute(q)
                con.commit()
                print("Modifications Completed")

            else:
                print("No Modifications done")

    else:
        print("No Applicant found with",ID, "ID")

def delete_applicant():

    ID=int(input("Enter ID to be deleted: "))
    query="select * from applicants where AID={}".format(ID)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>=1:
        for i in res:
            print("ID: ",i[0])
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Gender: ',i[3])
            print('Date Applied: ',i[4])
            print('Job Title: ',i[5])
            print("Qualification: ",i[6])
            print('Experience: ',i[7],'year(s)')
            print('Employment Status: ',i[8])
            print('Current Status: ',i[9])
            print('City: ',i[10])           
             
            print("Do you want to delete?")
            ans=input("(Y/N): ")
            if ans in "Yy":
                q="delete from applicants where AID={}".format(ID)
                cur.execute(q)
                con.commit()
                print("Record Deleted")
            else:
                print("No Record Deleted")
    else:
        print("No record found with", ID,"ID")

def search_applicant():
    ID=int(input("Enter Applicant ID to search: "))
    query="select * from applicants where AID={}".format(ID)
    cur.execute(query)
    data=cur.fetchall()
    if cur.rowcount>=1:
        for i in data:
            print('Name: ',i[1])
            print('Email: ',i[2])
            print('Gender: ',i[3])
            print('Date Applied: ',i[4])
            print('Job Title: ',i[5])
            print("Qualification: ",i[6])
            print('Experience: ',i[7],'year(s)')
            print('Employment Status: ',i[8])
            print('Current Status: ',i[9])
            print('City: ',i[10])
    else:
        print("No Applicant found with ID: ",ID)

