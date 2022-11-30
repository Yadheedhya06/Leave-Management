from socketserver import DatagramRequestHandler
import tkinter
import tkinter.messagebox as tk
from tkinter.font import Font
from easygui import *
from tkinter import *
from turtle import *
import random
import csv


def AdminLogin():
    message = "Enter Username and Password"
    title = "Admin Login"
    fieldnames = ["Username", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)
    if field[0] == 'admin' and field[1] == 'admin':
        tkinter.messagebox.showinfo("Admin Login", "Login Successfully")
        adminwindow()
    else:
        tk.showerror("Error info", "Incorrect username or password")


def EmployeeLogin():
    message = "Enter Employee ID and Password"
    title = "Employee Login"
    fieldnames = ["Employee ID", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)

    if not len(field[0] or field[1]) < 1:
        text_file = open("D:/Leave-Management- System/employee.csv")
        csvreader = csv.reader(text_file)
        data=[]
        for row in csvreader:
            data.append(row)
        print(data)

        for row in data:
            if(row[0]==field[0] and row[3]==field[1]):
                global login
                login = field[0]
                f = 1
                print("Success")
                tkinter.messagebox.showinfo("Employee Login", "Login Successfully")
                EmployeeLoginWindow() 
    else:
         print("Invalid")
         tk.showerror("Error info", "Incorrect employee id or password")



def Employeelogout():
    global login
    login = -1
    LoginWindow.destroy()


def EmployeeAllInformationWindow():
    global EmployeeAllInformationWindow
    EmployeeAllInformationWindow = Toplevel()
    my_text = Text(EmployeeAllInformationWindow, width = 40, height = 10, font = ("Helvetica", 16)) 
    my_text.pack(pady=20)
    text_file = open("D:/Leave-Management- System/employee.csv", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()



def WindowStatus():
    StatusWindow = Toplevel()
    label_1 = Label(StatusWindow, text="Employee ID=", fg="blue", justify=LEFT, font=("Calibri", 16))
    label_2 = Label(StatusWindow, text=leaveStatus[1], font=("Calibri", 16))
    label_3 = Label(StatusWindow, text="Type=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_4 = Label(StatusWindow, text=leaveStatus[2], font=("Calibri", 16))
    label_5 = Label(StatusWindow, text="start=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_6 = Label(StatusWindow, text=leaveStatus[3], font=("Calibri", 16))
    label_7 = Label(StatusWindow, text="end=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_8 = Label(StatusWindow, text=leaveStatus[4], font=("Calibri", 16))
    label_9 = Label(StatusWindow, text="Status:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_10 = Label(StatusWindow, text=leaveStatus[6], font=("Calibri", 16))
    label_11 = Label(StatusWindow, text="leave_id:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_12 = Label(StatusWindow, text=leaveStatus[0], font=("Calibri", 16))
    label_11.grid(row=0, column=0)
    label_12.grid(row=0, column=1)
    label_1.grid(row=1, column=0)
    label_2.grid(row=1, column=1)
    label_3.grid(row=2, column=0)
    label_4.grid(row=2, column=1)
    label_5.grid(row=3, column=0)
    label_6.grid(row=3, column=1)
    label_7.grid(row=4, column=0)
    label_8.grid(row=4, column=1)
    label_9.grid(row=5, column=0)
    label_10.grid(row=5, column=1)


def balance():
    global balance
    balance = Toplevel()
    my_text = Text(balance, width = 40, height = 10, font = ("Helvetica", 16)) 
    my_text.pack(pady=20)
    text_file = open("D:/Leave-Management- System/balance.csv", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def apply():
    message = "Enter the following details "
    title = "Leave Apply"
    fieldNames = ["Employee ID", "From", "To", "days"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    message1 = "Select type of leave"
    title1 = "Type of leave"
    choices = ["Sick leave", "Maternity leave", "Emergency leave",]
    choice = choicebox(message1, title1, choices)
    leaveid = random.randint(1, 1000)

    if str(choice) == "Sick leave":
       process_leave_choice(fieldValues, choice, leaveid, 1)
    elif str(choice) == "Maternity leave":
       process_leave_choice(fieldValues, choice, leaveid, 2)
    else:
       process_leave_choice(fieldValues, choice, leaveid, 3)


def process_leave_choice(fieldValues, choice, leaveid, rowIndex):
    text_file = open("D:/Leave-Management- System/balance.csv")
    csvreader = csv.reader(text_file)
    data=[]
    for row in csvreader:
         data.append(row)
    print(data)
    for row in data:
     if(len(row) < 1): continue
     if row[0] == fieldValues[0]:
         row[rowIndex] = int(row[rowIndex]) - int(fieldValues[3])
         if row[rowIndex] < 0:
            tk.showerror("Error info", "Ivalid Number of Leaves")
            return
    filename = "D:/Leave-Management- System/balance.csv"
    with open(filename, 'w') as file:
       for row in data:
         for x in row:
             file.write(str(x)+',')
         file.write('\n')
    text_file.close()
    text_file2 = open("D:/Leave-Management- System/status.csv", 'a')
    text_file2.write("\n"+str(leaveid) + "," +str(choice) + "," + fieldValues[0] + "," + fieldValues[1] + "," + fieldValues[2] + "," + fieldValues[3])
    text_file2.close()



def leavelist():
    global leavelist
    leavelist = Toplevel()
    my_text = Text(leavelist, width = 40, height = 10, font = ("Helvetica", 16)) 
    my_text.pack(pady=20)
    text_file = open("D:/Leave-Management- System/status.csv", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    


def registration():
    message = "Enter Details of Employee"
    title = "Registration"
    fieldNames = ["Employee ID", "Name", "Contact Number", "Password"]

    fieldValues = multpasswordbox(message, title, fieldNames)
 
    text_file = open("D:/Leave-Management- System/employee.csv", 'a')
    text_file.write(fieldValues[0]+","+fieldValues[1]+","+fieldValues[2]+","+fieldValues[3] +"\n")
    text_file.close()

    text_file2 = open("D:/Leave-Management- System/balance.csv", 'a')
    text_file2.write(fieldValues[0]+","+str(60)+","+str(60)+","+str(70)+"\n")
    text_file2.close()


def EmployeeLoginWindow():
    global LoginWindow
    LoginWindow = Toplevel()
    LoginWindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(LoginWindow, image=filename)
    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)

    submit = Button(LoginWindow, text='Submit Leave', command=apply, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    submit['font'] = BtnFont
    submit.pack(fill=X)

    LeaveBalance = Button(LoginWindow, text='Leave Balance', command=balance, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveBalance['font'] = BtnFont
    LeaveBalance.pack(fill=X)

    LogoutBtn = Button(LoginWindow, text='Logout', bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=Employeelogout)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    submit.pack()
    LeaveBalance.pack()
    LogoutBtn.pack()
    ExitBtn.pack()



def adminwindow():
    global adminmainwindow
    adminmainwindow = Toplevel()
    adminmainwindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(adminmainwindow, image=filename)

    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    informationEmployee = Button(adminmainwindow, text='All Employee information', command=EmployeeAllInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)



    LeaveListButton = Button(adminmainwindow, text='Leave approval list', command=leavelist, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveListButton['font'] = BtnFont
    LeaveListButton.pack(fill=X)

    LogoutBtn = Button(adminmainwindow, text='Logout', command=adminmainwindow.destroy, bd=12, relief=GROOVE, fg="red",
                     bg="#ffffb3",
                     font=("Calibri", 36, "bold"), pady=3)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)


    LeaveListButton.pack()
    ExitBtn.pack()


root = Tk()
root.wm_attributes('-fullscreen', '1')
root.title("Leave Management System")
root.iconbitmap(default="D:/Leave-Management- System/leavelogo.ico")
filename = PhotoImage(file="D:/Leave-Management- System/background.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
BtnFont = Font(family='Calibri(Body)', size=20)
MainLabel = Label(root, text="Leave Management System", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 36, "bold"), pady=3)
MainLabel.pack(fill=X)
im = PhotoImage(file="D:/Leave-Management- System/login.gif")

AdminLgnBtn = Button(root, text='Admin login',  bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=AdminLogin)
AdminLgnBtn['font'] = BtnFont
AdminLgnBtn.pack(fill=X)


LoginBtn = Button(root, text='Employee login', bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=EmployeeLogin)
LoginBtn['font'] = BtnFont
LoginBtn.pack(fill=X)


EmployeeRegistration = Button(root, text='Employee registration', command=registration, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
EmployeeRegistration['font'] = BtnFont
EmployeeRegistration.pack(fill=X)

ExitBtn = Button(root, text='Exit', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
ExitBtn['font'] = BtnFont
ExitBtn.pack(fill=X)
MainLabel.pack()
AdminLgnBtn.pack()
LoginBtn.pack()
EmployeeRegistration.pack()
ExitBtn.pack()


root.mainloop()
