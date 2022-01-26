from msilib.schema import CheckBox
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

#from checkbox import isChecked

#from checkbox import isChecked
class Login:
   def _init_(self,root) :
       self.root=root
       self.root.title("Login and registration system for apps")
       self.root.geometry("1366x700+0+0")
       self.root.resizable(False,False)
       self.loginform()
   def loginform(self):
       Frame_login= Frame(self.root,bg="white")
       Frame_login.place(x=0,y=0,height=700,width=1366)

       #self.img= ImageTk.PhotoImage(file="background-2.jpg")
      # img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
       frame_input=Frame(self.root,bg="white")
       frame_input.place(x=320,y=130,height=450,width=350)
       label1=Label(frame_input,text="Login here",font=('impact',32,'bold'),fg="black",bg="white")
       label1.place(x=75,y=20)
       label2=Label(frame_input,text="Username",font=('Goudy old style',32,'bold'),fg="orangered",bg="white")
       label2.place(x=30,y=95)
       self.email_txt=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
       self.email_txt.place(x=30,y=145,height=35,width=270)
       label3=Label(frame_input,text="Password",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
       label3.place(x=30,y=195)
       self.password=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
       self.password.place(x=30,y=245,height=35,width=270)
       btn1= Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
       btn1.place(x=125,y=305)
       btn2= Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
       btn2.place(x=90,y=340)
       btn3= Button(frame_input,text="Not Registered?Register",command=self.Register,cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
       btn3.place(x=110,y=390)
   def login(self):
       if self.email_txt.get()=="" or self.password.get()=="":
           messagebox.showerror("Error","All feilds are required",parent=self.root)
       else:
           try:
               con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
               cur=con.cursor(buffered=True)
               cur.execute('select * from register where emailid=%s and password=%s',(self.email_txt.get(),self.password.get()))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror('Error','Invalid username and password',parent=self.root)
                   self.loginclear()
                   self.email_txt.focus()
               else:
                   self.appscreen()
                   con.close()
           except Exception as es:
               messagebox.showerror('Error',f'Error Due to: {str(es)}',parent=self.root)
   def Register(self):
       Frame_login1=Frame(self.root,bg="white")
       Frame_login1.place(x=0,y=0,height=700,width=1366)
       frame_input2=Frame(self.root,bg="white")
       frame_input2.place(x=320,y=130,height=450,width=630)
       label1=Label(frame_input2,text="Register here",font=('impact',32,'bold'),fg="black",bg="white")
       label1.place(x=45,y=20)
       label2=Label(frame_input2,text="Username",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
       label2.place(x=30,y=95)
      
      
      
       self.entry=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
       self.entry.place(x=30,y=145,height=35,width=270)
      
      
      
       label3=Label(frame_input2,text="Password",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
       label3.place(x=30,y=195)
       self.entry2=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
       self.entry2.place(x=30,y=245,height=35,width=270)
       label4=Label(frame_input2,text="Email id",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
       label4.place(x=330,y=95)
       self.entry3=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
       self.entry3.place(x=330,y=145,height=35,width=270)
       label5=Label(frame_input2,text="confirm Password",font=('Gody old style',20,'bold'),fg="orangered",bg="white")
       label5.place(x=330,y=195)
       self.entry4=Entry(frame_input2,font=('times new roman',15,'bold'),bg="lightgray")
       self.entry4.place(x=330,y=245,height=35,width=270)
       btn2= Button(frame_input2,text="Register",command=self.register,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
       btn2.place(x=90,y=340)
       btn3= Button(frame_input2,text="Already Registered?login",command=self.loginform,cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
       btn3.place(x=110,y=390)
   def register(self):
       if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
           messagebox.showerror("Error","All feilds are required",parent=self.root)
          
       elif self.entry2.get()!=self.entry4.get():
           messagebox.showerror("Error","Password and confirm password should be same",parent=self.root)
       else:
          
           #try:
               con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
               cur=con.cursor(buffered=True)
               #cur.execute('select * from register where emailid=%s ',(self.entry3.get()))
               #row=cur.fetchall()
               #if row!=None:
                   #messagebox.showerror("Error","user already exists,please try with another email id",parent=self.root)
                   #self.regclear()
                   #self.entry.focus()
               #else:
                   #string= self.entry.get()
          

               cur.execute('INSERT INTO register VALUES("'+str(self.entry.get())+'","'+str(self.entry3.get())+'","'+str(self.entry2.get())+'","'+str(self.entry4.get())+'","'+str(0)+'","'+str(0)+'");')  
                  
               con.commit()
               con.close()
               #messagebox.showerror("register successful",parent=self.root)
              
               self.regclear()
           #except Exception as es:
               #messagebox.showerror("error",f"error due to:{str(es)}",parent=self.root)

   def isCheckedYoga(self):
       frame_inputt=Frame(self.root,bg="black")
       frame_inputt.place(x=500,y=500,height=300,width=400)
  
       if self.CheckVar1.get() == 1:
           label4=Label(frame_inputt,text="You achieved a streak in yoga",font=('times new roman',12,'bold'),fg="orangered",bg="white")
           label4.place(x=40,y=30)
           try:
               con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
               cur=con.cursor(buffered=True)
               #self.name=self.email_txt.get()
               #cur.execute('update register set YogaStreaks=YogaStreaks+1 where emailid=self.name ;')
              
               cur.execute('update register set YogaStreaks=YogaStreaks+1 where emailid=%s and password=%s',(self.email_txt.get(),self.password.get()))
               con.commit()
               #cur.execute("select * from register")
               #for i in cur:
                 #  print(i)
              
           except Exception as es:
               messagebox.showerror("error",f"error due to:{str(es)}",parent=self.root)
   def isCheckedHomework(self):
       frame_inputt=Frame(self.root,bg="black")
       frame_inputt.place(x=500,y=500,height=300,width=400)
  
       if self.CheckVar2.get() == 1:
           label4=Label(frame_inputt,text="You achieved a streak in homework",font=('times new roman',12,'bold'),fg="orangered",bg="white")
           label4.place(x=40,y=30)
           try:
               con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
               cur=con.cursor(buffered=True)
               #cur.execute('update register set HomeworkStreaks=HomeworkStreaks+1 where username="Nandani" ;')
               cur.execute('update register set HomeworkStreaks=HomeworkStreaks+1 where emailid=%s and password=%s',(self.email_txt.get(),self.password.get()))
               con.commit()
              
               #cur.execute("select * from register")
               #for i in cur:
                #   print(i)
              
           except Exception as es:
               messagebox.showerror("error",f"error due to:{str(es)}",parent=self.root)

   def displayStreaks(self):
       con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
       cur=con.cursor(buffered=True)
       sql='SELECT YogaStreaks,HomeworkStreaks FROM register where username="Krishna"'
       #sql=('SELECT YogaStreaks,HomeworkStreaks FROM register where emailid=%s',(self.email_txt.get()))
       #cur.execute('SELECT YogaStreaks,HomeworkStreaks FROM register where emailid=%s',(self.email_txt.get()))
       cur.execute(sql)
       rows=cur.fetchall()
      
       Frame_loginn=Frame(self.root,bg="white")
       Frame_loginn.place(x=500,y=500,height=450,width=630)
       tv=ttk.Treeview(Frame_loginn,columns=(1,2),show="headings",height=7)
       tv.pack()
       tv.heading(1,text="YogaStreaks")
       tv.heading(2,text="HomeworkStreaks")
       for i in rows:
           tv.insert('','end',values=i)


  

   def appscreen(self):
       Frame_login=Frame(self.root,bg="white")
       Frame_login.place(x=0,y=0,height=700,width=1366)
       label1=Label(Frame_login,text="Welcome to Habit Tracker",font=('times new roman',32,'bold'),fg="black",bg="white")
       label1.place(x=375,y=100)    
       label2=Label(Frame_login,text="Consistency is the key",font=('times new roman',12,'bold'),fg="black",bg="white")
       label2.place(x=700,y=160)
       label3=Label(Frame_login,text="Select the tasks performed",font=('times new roman',25,'bold'),fg="black",bg="white")
       label3.place(x=340,y=220)
       btn2= Button(Frame_login,text="log out",command=self.loginform,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
       btn2.place(x=1000,y=10)
       self.CheckVar1 = BooleanVar()
       self.CheckVar2 = BooleanVar()
       Checkbutton(Frame_login, text="Yoga", variable=self.CheckVar1, onvalue=1, offvalue=0, command=self.isCheckedYoga).place(x=400,y=500)
      
       Checkbutton(Frame_login, text="Homework", variable=self.CheckVar2, onvalue=1, offvalue=0, command=self.isCheckedHomework).place(x=400,y=550)
      
       btn3= Button(Frame_login,text="Check Streaks",command=self.displayStreaks,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
       btn3.place(x=900,y=350)
      

          

   def regclear(self):
       self.entry.delete(0,END)
       self.entry2.delete(0,END)
       self.entry3.delete(0,END)
       self.entry4.delete(0,END)
   def loginclear(self):
       self.email_txt.delete(0,END)
       self.password.delete(0,END)

root=Tk()
ob=Login(root)
root.mainloop()

