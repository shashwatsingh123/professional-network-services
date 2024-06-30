import mysql.connector as ms
from tabulate import tabulate

con=ms.connect(host='localhost', user='root', passwd='abc@123', database='job')
cur=con.cursor()

def applicant_report():
    query="select * from applicants"
    cur.execute(query)
    data=cur.fetchall()
    head=['ID','Name','Email','Sex','DateApp.','JobTitle',\
          'Qualification','Exp.','Emp.Status','Current Status','City']
    print(tabulate(tabular_data=data, headers=head,tablefmt='grid'))

def company_report():
    query="select * from company"
    cur.execute(query)
    data=cur.fetchall()
    head=['ID','Name','Email','Qualification','JobTitle',\
          'Exp.','Vacancy','City']
    print(tabulate(tabular_data=data, headers=head,tablefmt='grid'))

def final_report():
    q="select * from applied"
    cur.execute(q)
    res=cur.fetchall()
    head=['Applicant ID','Name','Company ID','Job Title',"City"]
    print(tabulate(tabular_data=res, headers=head,tablefmt='grid'))

def start_report():
        print("What do you want to see?")
        print("1.Company Report\n2.Applicant Report\n3.Final Report\n4.Exit")
        c2=int(input("Enter your choice: "))
        if c2==1:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            company_report()
            print()
        elif c2==2:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            applicant_report()
            print()
        elif c2==3:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            final_report()
            print()
        elif c2==4:
            print()
            print("PROFESSIONAL NETWORK SERVICES")
            import Main as menu
            menu.main_menu()
            print()
