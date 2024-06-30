import mysql.connector as ms
import Applicants as app
import Company as comp
import Report as rep
con=ms.connect(host='localhost', user='root',passwd="abc@123", database='job',)
cur=con.cursor()

def main_menu():
    print()
    print("Welcome to PROFESSIONAL NETWORK SERVICES")
    print()
    print("A service where applicats can search for hiring companies and vice versa!")
    print()
    print("What do you want to do?")
    print("1.Applicants\n2.Company\n3.Report")
    c1=int(input("Enter your choice: "))
    if c1==1:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        app.start_applicants()
        print()
    elif c1==2:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        comp.start_company()
        print()
    elif c1==3:
        print()
        print("PROFESSIONAL NETWORK SERVICES")
        rep.start_report()
        print()
    else:
        print("Enter valid choice!")
        print()

while True:
    print("**"*30)
    print(" "*15,"PROFESSIONAL NETEWORK SERVICES")
    print("**"*30)
    main_menu()
    print()





