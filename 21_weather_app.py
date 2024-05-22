from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=64def917d881a59c10f21493358b2443").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    # temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    temp_label1.config(text=round(data["main"]["temp"]-273.15,2))
    pre_label1.config(text=data["main"]["pressure"])






win=Tk()
win.title("Durjoy")
win.config(bg='blue')
win.geometry('500x570')

#creating a Label 
name_label=Label(win,text="Weather App",font=('Times New Roman',35,'bold'))
name_label.place(x=25,y=50,height=50,width=450)

#CREATING COMBOBOX
city_name=StringVar()
States_name=[
                "Dhaka",
                "Chittagong",
                "Khulna",
                "Rajshahi",
                "Barisal",
                "Sylhet",
                "Rangpur",
                "Mymensingh"
            ]
com=ttk.Combobox(win,text="Weather App",values=States_name,font=("Time new Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#creating a button()
done_button=Button(win,text="Check",font=("Time new Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

#creating a Label 
w_label=Label(win,text="Weather Climate",font=('Times New Roman',20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=('Times New Roman',20))
w_label1.place(x=250,y=260,height=50,width=210)

#creating a Label 
wb_label=Label(win,text="Weather Description",font=('Times New Roman',17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text="",font=('Times New Roman',17))
wb_label1.place(x=250,y=330,height=50,width=210)

#creating a Label 
temp_label=Label(win,text="Temperature",font=('Times New Roman',17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=('Times New Roman',17))
temp_label1.place(x=250,y=400,height=50,width=210)

#creating a Label 
pre_label=Label(win,text="Pressure",font=('Times New Roman',17))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1=Label(win,text="",font=('Times New Roman',17))
pre_label1.place(x=250,y=470,height=50,width=210)







win.mainloop()