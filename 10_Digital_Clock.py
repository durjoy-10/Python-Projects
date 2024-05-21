from tkinter import *
import datetime
def date_time():
    #For time
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    amORpm=time.strftime('%p')
    
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')
    
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_amORpm.config(text=amORpm)
    
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    

    lab_hr.after(200,date_time) #It changes the time after 200 ms and call itself



clock= Tk()
clock.title("      ****** DIGITAL CLOCK ******")
clock.geometry('1000x500')
clock.config(bg='yellow')

#                              Time
#___________________________________________________________________________________
lab_hr=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt=Label(clock,text="HOUR",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_hr_txt.place(x=120,y=190,height=40,width=100)



lab_min=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt=Label(clock,text="MIN.",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_min_txt.place(x=340,y=190,height=40,width=100)



lab_sec=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt=Label(clock,text="SEC.",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_sec_txt.place(x=560,y=190,height=40,width=100)



lab_amORpm=Label(clock,text="00",font=('Time New Roman',50,"bold"),bg='red',fg='white')
lab_amORpm.place(x=780,y=50,height=110,width=100)
lab_amORpm_txt=Label(clock,text="AM/PM",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_amORpm_txt.place(x=780,y=190,height=40,width=100)

#                                    date
# ________________________________________________________________________________________

lab_date=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt=Label(clock,text="DATE",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_mon=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_mon.place(x=340,y=270,height=110,width=100)
lab_mon_txt=Label(clock,text="MONTH",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_mon_txt.place(x=340,y=410,height=40,width=100)

lab_year=Label(clock,text="00",font=('Time New Roman',60,"bold"),bg='red',fg='white')
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt=Label(clock,text="YEAR",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_year_txt.place(x=560,y=410,height=40,width=100)


lab_day=Label(clock,text="00",font=('Time New Roman',35,"bold"),bg='red',fg='white')
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt=Label(clock,text="DAY",font=('Time New Roman',20,"bold"),bg='red',fg='white')
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()

clock.mainloop()