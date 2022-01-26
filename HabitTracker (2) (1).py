
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox,filedialog
import mysql.connector


import tkinter as tk
class Login:
    def __init__(self,root) :
        self.root=root
        
        self.root.title("Habit Tracker")
        self.root.geometry("1366x700+0+0") 
        self.root.resizable(False,False) 
        self.loginform()
       
    def loginform(self):
        Frame_login= Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366) 

        self.img= ImageTk.PhotoImage(file="habitt.jpeg") 
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
        frame_input=Frame(self.root,bg="white") 
        frame_input.place(x=220,y=130,height=450,width=350)
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
        #btn1= Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
       # btn1.place(x=125,y=305)
        btn2= Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)
        btn3= Button(frame_input,text="Not Registered? Register",command=self.Register,cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        btn3.place(x=110,y=390)
    def login(self):
        if self.email_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
                cur=con.cursor(buffered=True)
                cur.execute('select * from register where username=%s and password=%s',(self.email_txt.get(),self.password.get()))
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
               # messagebox.showinfo("register successful",parent=self.root)
                messagebox.showinfo("Yayy!","You are successfully registered",parent=self.root)
                
                self.regclear()
            #except Exception as es:
                #messagebox.showerror("error",f"error due to:{str(es)}",parent=self.root)
    
    def isAdded(self):
        print(1)       
        username=self.email_txt.get()
        print(username)
        habit1="Swimming"
        print(self.CheckVar3.get())
        if (self.CheckVar3.get() == 1):
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            cur.execute('select habits from nandani where habits="Swimming"')
            #cur.execute("select habits from "+str(username)+"  where habits= "+"'Swimming'")
            row=cur.fetchone()
            if row==None:
                #cur.execute('INSERT INTO nandani VALUES(')
                cur.execute('INSERT INTO nandani VALUES ("' +str(habit1)+ '",'+str('0')+ ',"'+str('I007')+'",'+str('NULL')+')')
                con.commit()
                print("inserted")
            else:
                print("no")
        habit2="Quit smoking"
        if self.CheckVar4.get() == 1:
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            #cur.execute('select habits from nandani where habits="Swimming"')
            cur.execute("select habits from "+str(username)+"  where habits= "+"'Quit smoking'")
            row=cur.fetchone()
            if row==None:
                cur.execute('INSERT INTO '+str(username)+ ' VALUES ("' +str(habit2)+ '",'+str('0')+ ')')
                con.commit()
                print("inserted")
        habit3="Quit drinking"
        if self.CheckVar5.get() == 1:
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            #cur.execute('select habits from nandani where habits="Swimming"')
            cur.execute("select habits from "+str(username)+"  where habits= "+"'Quit drinking'")
            row=cur.fetchone()
            if row==None:
                cur.execute('INSERT INTO '+str(username)+ ' VALUES ("' +str(habit3)+ '",'+str('0')+ ')')
                con.commit()
                print("inserted")
        habit4="No fast food"
        if self.CheckVar3.get() == 1:
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            #cur.execute('select habits from nandani where habits="Swimming"')
            cur.execute("select habits from "+str(username)+"  where habits= "+"'No fast food'")
            row=cur.fetchone()
            if row==None:
                cur.execute('INSERT INTO '+str(username)+ ' VALUES ("' +str(habit4)+ '",'+str('0')+ ')')
                con.commit()
                print("inserted")
        habit5="Breakfast"
        if self.CheckVar4.get() == 1:
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            #cur.execute('select habits from nandani where habits="Swimming"')
            cur.execute("select habits from "+str(username)+"  where habits= "+"'Breakfast'")
            row=cur.fetchone()
            if row==None:
                cur.execute('INSERT INTO '+str(username)+ ' VALUES ("' +str(habit5)+ '",'+str('0')+ ')')
                con.commit()
                print("inserted")
        habit6="8 hours sleep"
        if self.CheckVar5.get() == 1:
            print(1)           
            con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
            cur=con.cursor(buffered=True)
            cur.execute("CREATE TABLE IF NOT EXISTS "+str(username)+" (habits varchar(20) not null, streaks int(5) DEFAULT '0');")
            #cur.execute('select habits from nandani where habits="Swimming"')
            cur.execute("select habits from "+str(username)+"  where habits= "+"'8 hours sleep'")
            row=cur.fetchone()
            if row==None:
                cur.execute('INSERT INTO '+str(username)+ ' VALUES ("' +str(habit6)+ '",'+str('0')+ ')')
                con.commit()
                print("inserted")       
    def removethis2(self):
        self.frame_inputtt.destroy()
        
    def on_close(self):
        response=messagebox.askyesno('Exit','Are you sure you want to exit?')
        if response:
            self.New_Window.destroy() 

          
            
    def newGoals(self):
        self.New_Window = Toplevel()
        self.New_Window.geometry("1366x700+0+0") 
        #self.New_Window.protocol('WM_DELETE_WINDOW',self.on_close)
        frame_inputtt=Frame(self.New_Window,bg="white") 
        frame_inputtt.place(x=0,y=0,height=1500,width=2000)
        self.CheckVar3 = BooleanVar()
        self.CheckVar4 = BooleanVar()
        self.CheckVar5 = BooleanVar()
        self.CheckVar6 = BooleanVar()
        self.CheckVar7 = BooleanVar()
        self.CheckVar8 = BooleanVar()
        self.CheckVar9 = BooleanVar()
        self.CheckVar10 = BooleanVar()
        
        Checkbutton(frame_inputtt, text="Swimming", variable=self.CheckVar3, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=30)
        Checkbutton(frame_inputtt, text="Quit smoking", variable=self.CheckVar4, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=50)
        Checkbutton(frame_inputtt, text="Quit drinking", variable=self.CheckVar5, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=70)
        Checkbutton(frame_inputtt, text="No fast food", variable=self.CheckVar6, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=90)
        Checkbutton(frame_inputtt, text="Breakfast", variable=self.CheckVar7, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=110)
        Checkbutton(frame_inputtt, text="8 hours sleep", variable=self.CheckVar8, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=130)
        Checkbutton(frame_inputtt, text="Screen time limited", variable=self.CheckVar9, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=150)
        Checkbutton(frame_inputtt, text="Sports", variable=self.CheckVar10, onvalue=1, offvalue=0, command=self.isAdded).place(x=40,y=170)
        print(self.CheckVar3.get())
        #butt = Button(New_Window, text="Push me2", command=self.removethis2)
        #butt.place(x=800,y=450)
        
        
        


    
    def removethis(self):
        self.Frame_loginn.destroy()
    

    def displayStreaks(self):
        con= mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cur=con.cursor(buffered=True)
        sql='SELECT * FROM nandani'
        
        #sql=('SELECT YogaStreaks,HomeworkStreaks FROM register where emailid=%s',self.email_txt.get())
        #cur.execute('SELECT YogaStreaks,HomeworkStreaks FROM register where emailid=%s',self.email_txt.get())
        cur.execute(sql)
        rows=cur.fetchall()
        self.Display_Window = Toplevel()
        self.Display_Window.geometry("1366x700+0+0") 
        

        self.Frame_loginn=Frame(self.Display_Window,bg="white")
        self.Frame_loginn.place(x=0,y=0,height=2000,width=1500)
        tv=ttk.Treeview(self.Frame_loginn,columns=(1,2),show="headings",height=7)
        tv.pack()
        tv.heading(1,text="Habits")
        tv.heading(2,text="Streaks")
        for i in rows:
            tv.insert('','end',values=i)
        #butt = Button(self.root, text="Push me", command=self.removethis)
        #butt.place(x=1000,y=450)
        
    
                
        
    

    def togglecheck(self,event):
        mydb=mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cursor=mydb.cursor()

        rowid=self.trv.identify_row(event.y)
        tag =self.trv.item(rowid,"tags")[0]
        tags=list(self.trv.item(rowid,"tags"))
        tags.remove(tag)
        self.trv.item(rowid,tags=tags)
    
        if tag=="checked":
            self.trv.item(rowid,tags="unchecked")
        
        else:
            self.trv.item(rowid,tags="checked")
            hey=rowid
            print(rowid)
            print(hey)

        #cursor.execute("update nandani set streaks=streaks+1 where habits= "+"'Swimming'")
        #if(rowid=='I005'):
            #cursor.execute("update nandani set streaks=streaks+1 where rowid= "+"'I005'")
        #cursor.execute("update nandani set streaks=streaks+1 where rowid= "+rowid)
        #cursor.execute('update nandani set streaks=streaks+1 where rowid=%s ',(str(rowid)))
            cursor.execute('update nandani set streaks=streaks+1 where rowid="'+str(rowid)+'"')
        #cur.execute('INSERT INTO register VALUES("'+str(self.entry.get())+'","'+str(self.entry3.get())+'","'+str(self.entry2.get())+'","'+str(self.entry4.get())+'","'+str(0)+'","'+str(0)+'");')  
            mydb.commit()
            

    def update(self):
        mydb=mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cursor=mydb.cursor()
        self.Update_Window = Toplevel()
        self.Update_Window.geometry("1366x700+0+0") 

        #wrapper1=LabelFrame(root,text="Select today's finished tasks")
        
        wrapper1=LabelFrame(self.Update_Window,text="Select today's finished tasks")
        wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
        im_checked= ImageTk.PhotoImage(Image.open("checked1.png"))
        im_unchecked= ImageTk.PhotoImage(Image.open("unchecked1.png"))
        #im_checked= ImageTk.PhotoImage(file="checked.jpg") 
        #im_unchecked= ImageTk.PhotoImage(file="unchecked.jpg") 
        self.trv=ttk.Treeview(wrapper1,columns=(1,2))
        style=ttk.Style(self.trv)
        style.configure('Treeview',rowheight=30)
        self.trv.tag_configure('checked',image=im_checked)
        self.trv.tag_configure('unchecked',image=im_unchecked)

        self.trv.pack()
        self.trv.heading('#0',text="")
        self.trv.heading('#1',text="habits")
        self.trv.heading('#2',text="streaks")
#trv.heading('#3',text="last name")
#trv.heading('#4',text="age")

#trv.bind('<Double 1>',getrow)
        self.trv.bind('<Button 1>',self.togglecheck)


        query="SELECT * FROM nandani"
        cursor.execute(query)
        rows=cursor.fetchall()
        for i in rows:
            self.trv.insert('','end',values=i,tags="unchecked")

    def profile(self):
        self.Profile_Window = Toplevel()
        self.Profile_Window.geometry("1366x700+0+0") 
        #self.Profile_Window.protocol('WM_DELETE_WINDOW',self.on_close2)
        mydb=mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cursor=mydb.cursor()
        Frame_Profile= Frame(self.Profile_Window,bg="white")
        Frame_Profile.place(x=0,y=0,height=1500,width=2000) 
        usernameDisplay=Label(Frame_Profile,text="Nandani",font=('times new roman','22','bold'),fg="orangered",bg="white")
        usernameDisplay.place(x=200,y=40)
        achievementsDisplay=Label(Frame_Profile,text="Achievements",font=('times new roman','22','bold'),fg="black",bg="white")
        achievementsDisplay.place(x=200,y=200)
        cursor.execute('select crown from nandani where crown is not null')
        rows=cursor.fetchall()
        
        j=0
        for i in rows:
            j=j+1
            print(j)
        if(j==1):
            self.img= ImageTk.PhotoImage(file="crown1.jpg") 
            img=Label(Frame_Profile,image=self.img).place(x=300,y=300,width=120,height=120)
        if(j==2):
            self.img= ImageTk.PhotoImage(file="2crowns.png") 
            img=Label(Frame_Profile,image=self.img).place(x=300,y=300,width=200,height=120)
        if(j==3):
            self.img= ImageTk.PhotoImage(file="3crowns.png") 
            img=Label(Frame_Profile,image=self.img).place(x=300,y=300,width=300,height=120)
        
            
        
             




    def claimcrown(self):
        mydb=mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cursor=mydb.cursor()
        cursor.execute('UPDATE register SET Crowns="'+str(self.k)+'" WHERE username="Nandani"')
        #cur.execute("select habits from "+str(username)+"  where habits= "+"'8 hours sleep'")
        mydb.commit()
        #cursor.execute('update register set Crowns= where rowid="'+str(rowid)+'"')


    def achievements(self):
        self.New_Windoww = Toplevel()
        self.New_Windoww.geometry("1366x700+0+0") 
        #self.New_Windoww.protocol('WM_DELETE_WINDOW',self.on_close2)
        mydb=mysql.connector.connect(host="localhost",user="Nandani",passwd="MiniProjecthehe1.",database="pythongui")
        cursor=mydb.cursor()
        Frame_login= Frame(self.New_Windoww,bg="white")
        Frame_login.place(x=0,y=0,height=1500,width=2000) 
        
        self.img= ImageTk.PhotoImage(file="crown1.jpg") 
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=120,height=120)
        crownlabel=Label(Frame_login,text="REGAL\n Earn 1 crown per habit if streaks greater than 15",font=('times new roman','22','bold'),fg="black",bg="white")
        crownlabel.place(x=200,y=40)
        cursor.execute('SELECT streaks FROM nandani WHERE streaks>7 AND crown=1')
        rows=cursor.fetchall()
        j=0
        for i in rows:
            j=j+1
            print(j)

        cursor.execute('UPDATE nandani SET crown=1 WHERE streaks>7 AND crown is null')
        print("yes")
        mydb.commit()
        
        cursor.execute('SELECT streaks FROM nandani WHERE streaks>7 AND crown=1')
        rows=cursor.fetchall()
        self.k=0
        for i in rows:
            print(i)
            self.k=self.k+1
            print(self.k)
        if(self.k>j):
            print(str(self.k-j)+"new crowns")
            claimcrown= Button(Frame_login,text="claim crown",command=self.claimcrown,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
            claimcrown.place(x=800,y=40)

        

        self.img2= ImageTk.PhotoImage(file="bronze1.jpg") 
        img2=Label(Frame_login,image=self.img2).place(x=0,y=120,width=120,height=120)
        bronzelabel=Label(Frame_login,text="BRONZE LEAGUE\n Enter the Bronze league if 1/4 habits streaks greater than 15",font=('times new roman','22','bold'),fg="black",bg="white")
        bronzelabel.place(x=200,y=150)


        self.img3= ImageTk.PhotoImage(file="silver1.jpg") 
        img3=Label(Frame_login,image=self.img3).place(x=0,y=240,width=120,height=120)
        silverlabel=Label(Frame_login,text="SILVER LEAGUE\n Enter the Silver league if 1/2 habits streaks greater than 15",font=('times new roman','22','bold'),fg="black",bg="white")
        silverlabel.place(x=200,y=260)

        self.img4= ImageTk.PhotoImage(file="gold1.jpg") 
        img4=Label(Frame_login,image=self.img4).place(x=0,y=360,width=120,height=120)
        goldlabel=Label(Frame_login,text="GOLD LEAGUE\n Enter the Gold league if 3/4 habits streaks greater than 15",font=('times new roman','22','bold'),fg="black",bg="white")
        goldlabel.place(x=200,y=370)

        self.img5= ImageTk.PhotoImage(file="diamond1.jpg") 
        img5=Label(Frame_login,image=self.img5).place(x=0,y=480,width=120,height=120)
        diamondlabel=Label(Frame_login,text="DIAMOND LEAGUE\n Enter the Diamond league if all habits streaks greater than 15",font=('times new roman','22','bold'),fg="black",bg="white")
        diamondlabel.place(x=200,y=480)

        self.img6= ImageTk.PhotoImage(file="fire1.jpg") 
        img6=Label(Frame_login,image=self.img6).place(x=0,y=600,width=120,height=120)
        firelabel=Label(Frame_login,text="WILDFIRE\n 1 wildfire per 7 streaks",font=('times new roman','22','bold'),fg="black",bg="white")
        firelabel.place(x=400,y=590)




    def appscreen(self):
        #self.appscreen_window = Toplevel()
        #self.appscreen_window.geometry("1366x700+0+0")
        #Frame_login=Frame(self.appscreen_window,bg="white") 

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        self.img= ImageTk.PhotoImage(file="appscreen.jpg") 
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
        label1=Label(Frame_login,text="Welcome to Habit Tracker",font=('times new roman',32,'bold'),fg="black",bg="white")
        label1.place(x=375,y=100)     
        label2=Label(Frame_login,text="Consistency is the key",font=('times new roman',12,'bold'),fg="black",bg="white")
        label2.place(x=700,y=160)
        #label3=Label(Frame_login,text="Select the tasks performed",font=('times new roman',25,'bold'),fg="black",bg="white")
        #label3.place(x=340,y=220)
        btn4= Button(Frame_login,text="Select tasks",command=self.update,cursor='hand2',font=('calibri',15),bg="white",fg="orangered",bd=0)
        btn4.place(x=320,y=550)
        
        btn3= Button(Frame_login,text="Add new goals",command=self.newGoals,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn3.place(x=450,y=550)
        
        btn3= Button(Frame_login,text="Check Streaks",command=self.displayStreaks,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn3.place(x=650,y=550)
        btn5= Button(Frame_login,text="Achievements",command=self.achievements,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn5.place(x=850,y=550)
        
        btn2= Button(Frame_login,text="log out",command=self.loginform,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn2.place(x=1050,y=550)
        btn2= Button(Frame_login,text="Profile",command=self.profile,cursor='hand2',font=('times new roman',15),bg="white",fg="orangered",bd=0,width=15,height=1)
        btn2.place(x=140,y=550)
            

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
