from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sympy
import math

class manish:
    def clear(self):
        self.entry1.delete(0,END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
    def clear2(self):
        self.entry6.delete(0,END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)
        self.entry9.delete(0, END)
        self.entry10.delete(0, END)

    def submit1(self):
        final_message = []
        b1 = ""
        c1 = ""

        message2 = (self.entry6.get())
        p12 = (self.entry7.get())
        q12 = (self.entry8.get())
        if (message2 == "" or p12 == "" or q12 == ""):
            messagebox.showinfo("message", "Please enter detail")

        elif (message2.isnumeric() == True):
            messagebox.showinfo("message", "Please enter string text")
        elif (p12.isalpha() == True or q12.isalpha() == True):
            messagebox.showinfo("message", "Please enter numeric value")
        elif (p12==q12):
            messagebox.showinfo("message", "You can not enter same prime number")

        elif (p12 == "3" or p12 == "5" or p12 == "7" or q12 == "3" or q12 == "5" or q12 == "7"):
            messagebox.showinfo("message", "Please enter strong prime number")


        else:
            message = (self.entry6.get())

            p1 = int(self.entry7.get())
            q1= int(self.entry8.get())
            if (sympy.isprime(p1) == True) and (sympy.isprime(q1) == True):
                m1 = p1
                m2 = q1
                phi1 = (m1 - 1) * (m2 - 1)
                n1 = p1 * q1

                for i in range(1, 100000000000 + 1):
                    if (math.gcd(i, phi1) == 1 and 1 < i and i < phi1):
                        e1 = i

                        break;

                for i in range(1, 100000000000+ 1):
                    if (i * e1 % phi1 == 1):
                        d1 = i
                        # print("value of d=",d)
                        break;
                for i in message:
                    p1 = ord(i)
                    k = (p1 ** e1 % n1)
                    c1 = c1 + str(k)
                    # print("value of ciphertext=",k)

                    final_message.append((k ** d1 % n1))
                    # print("final.message=",final_message)
                for i in final_message:
                    b = chr(i)
                    b1 = b1 + b

                self.entry9.insert(0, c1)
                self.entry10.insert(0, b1)
            else:
                messagebox.showinfo("message", "Please enter prime number")

    def submit(self):


        message1 = (self.entry1.get())
        p1=(self.entry2.get())
        q1=(self.entry3.get())
        if(message1==""or p1=="" or q1==""):
            messagebox.showinfo("message","please enter detail")
        elif(message1.isalpha()==True or p1.isalpha()==True or q1.isalpha==True):
            messagebox.showinfo("message","please enter numeric value")
        elif(p1==q1):
            messagebox.showinfo("message","You can not enter same prime number")
        else:
            message = int(self.entry1.get())
            p = int(self.entry2.get())
            q = int(self.entry3.get())
            if (sympy.isprime(p) == True) and (sympy.isprime(q) == True):
                m1 = p
                m2 = q
                phi = (m1 - 1) * (m2 - 1)
                n = p * q

                for i in range(1, 10000000000 + 1):
                    if (math.gcd(i, phi) == 1 and 1 < i and i < phi):
                        e = i
                        break;

                for i in range(1, 100000000000 + 1):
                    if (i * e % phi == 1):
                        d = i
                        break;

                if (message < n):
                    c = message ** e % n
                    final_message = (c ** d % n)
                    self.entry4.insert(0, c)
                    self.entry5.insert(0, final_message)
                else:
                    messagebox.showinfo("message", "The product of two prime number is small")

            else:
                messagebox.showinfo("message", "Please enter prime number")

    def __init__(self):
        self.window=Tk()
        self.window.geometry("820x500")
        self.window.resizable(FALSE,FALSE)


        self.font=Font(family="Times New Roman",size=14,weight="bold",slant="italic",underline=1)
        self.font1 = Font(family="Times New Roman", size=30, weight="bold", slant="italic",underline=1)
        self.font2 = Font(family="Times New Roman", size=10, weight="bold", slant="italic", underline=0)
        self.frame1=Frame(self.window,width=820,height=100,bg="blue",bd=8,relief="sunken")
        self.frame2 = Frame(self.window, width=400, height=200,bg="pink",bd=6,relief="sunken")
        self.frame3 = Frame(self.window, width=400, height=100,bg="orange",bd=6,relief="sunken")
        self.frame4 = Frame(self.window, width=420, height=200, bg="green",bd=6,relief="sunken")
        self.frame5 = Frame(self.window, width=420, height=100, bg="maroon",bd=6,relief="sunken")
        self.frame6 = Frame(self.window, width=820, height=500, bg="gold",bd=6,relief="sunken")

        self.frame1.place(x=0,y=0)
        self.frame2.place(x=0, y=100)
        self.frame3.place(x=0, y=300)
        self.frame4.place(x=400, y=100)
        self.frame5.place(x=400, y=300)
        self.frame6.place(x=0, y=400)

        self.lb=Label(self.window,text="RSA ALGORITHM",bg="blue",font=self.font1)

        self.lb1=Label(self.window,text="Enter Message",bg="pink",font=self.font)
        self.lb2 = Label(self.window, text="Enter First Prime Number", bg="pink",font=self.font)
        self.lb3 = Label(self.window, text="Enter Second Prime Number", bg="pink",font=self.font)
        self.lb4 = Label(self.window, text="CipherText", bg="orange",font=self.font)
        self.lb5 = Label(self.window, text="Message", bg="orange",font=self.font)
        self.lb6 = Label(self.window, text="Enter Message", bg="green", font=self.font)
        self.lb7 = Label(self.window, text="Enter First Prime Number", bg="green", font=self.font)
        self.lb8 = Label(self.window, text="Enter Second Prime Number", bg="green", font=self.font)
        self.lb9 = Label(self.window, text="CipherText", bg="maroon", font=self.font)
        self.lb10 = Label(self.window, text="Message", bg="maroon", font=self.font)
        self.lb11 = Label(self.window, text="This section enter only numeric message:-", bg="blue",font=self.font)
        self.lb12 = Label(self.window, text="This section enter only string message:-", bg="blue",font=self.font)
        self.lb13 = Label(self.window, text="Note:- in this section we can not put 3,5,7 prime number", bg="gold")
        self.lb14 = Label(self.window, text="According to RSA algorithm we can not use same prime number in both the input prime number textfield", bg="gold")



        self.entry1=Entry(self.window,width="23",bd="4",relief="sunken")
        self.entry2 = Entry(self.window,width="23",bd="4",relief="sunken")
        self.entry3 = Entry(self.window,width="23",bd="4",relief="sunken")
        self.entry4 = Entry(self.window,width="33",bd="4",relief="sunken")
        self.entry5 = Entry(self.window,width="33",bd="4",relief="sunken")
        self.entry6 = Entry(self.window,width="26",bd="4",relief="sunken")
        self.entry7 = Entry(self.window,width="26",bd="4",relief="sunken")
        self.entry8 = Entry(self.window,width="26",bd="4",relief="sunken")
        self.entry9 = Entry(self.window,width="40",bd="4",relief="sunken")
        self.entry10 = Entry(self.window,width="40",bd="4",relief="sunken")

        self.bt1=Button(self.window,text="Submit",font=self.font2,bg="light sky blue",command=self.submit)
        self.bt2 = Button(self.window, text="clear ", font=self.font2, bg="light sky blue", command=self.clear)
        self.bt3 = Button(self.window, text="Submit", font=self.font2, bg="light sky blue",command=self.submit1)
        self.bt4 = Button(self.window, text="clear ", font=self.font2, bg="light sky blue", command=self.clear2)

        self.lb.place(x=200, y=15)
        self.lb1.place(x=10,y=110)
        self.lb2.place(x=10, y=150)
        self.lb3.place(x=10, y=190)
        self.lb4.place(x=10, y=310)
        self.lb5.place(x=10, y=350)
        self.lb6.place(x=410, y=110)
        self.lb7.place(x=410, y=150)
        self.lb8.place(x=410 ,y=190)
        self.lb9.place(x=410, y=310)
        self.lb10.place(x=410, y=350)
        self.lb11.place(x=5, y=65)
        self.lb12.place(x=420, y=65)
        self.lb13.place(x=400, y=410)
        self.lb14.place(x=20, y=450)



        self.entry1.place(x=250,y=115)
        self.entry2.place(x=250, y=155)
        self.entry3.place(x=250, y=195)
        self.entry4.place(x=160, y=310)
        self.entry5.place(x=160, y=350)
        self.entry6.place(x=650, y=115)
        self.entry7.place(x=650, y=155)
        self.entry8.place(x=650, y=195)
        self.entry9.place(x=530, y=310)
        self.entry10.place(x=530, y=350)

        self.bt1.place(x=170,y=250)
        self.bt2.place(x=240, y=250)
        self.bt3.place(x=530, y=250)
        self.bt4.place(x=600, y=250)

        self.window.mainloop()
obj=manish()