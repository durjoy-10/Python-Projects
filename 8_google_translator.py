import pyttsx3
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def voice(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=combo_source.get()
    d=combo_destination.get()
    msg=source_txt.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    destination_txt.delete(1.0,END)
    destination_txt.insert(END,textget)

def source_voice():
    s_msg=source_txt.get(1.0,END)
    voice(s_msg)
    
def destination_voice():
    s=combo_source.get()
    d=combo_destination.get()
    msg=source_txt.get(1.0,END)
    d_msg=change(text=msg,src=s,dest=d)
    # destination_txt.delete(1.0,END)
    # d_msg=destination_txt.insert(END,textget)
    voice(d_msg)


root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='blue')

leb_txt=Label(root,text="Translator",font=("Time new roman",20,"bold"),bg='white')
leb_txt.place(x=150,y=40,height=40,width=200)

frame=Frame(root).pack(side=BOTTOM)

leb_txt=Label(root,text="Source Text:",font=("Time new roman",10,"bold"),fg='black',bg='white')
leb_txt.place(x=10,y=95,height=20,width=100)

source_txt=Text(frame,font=("Time new roman",10,"bold"),wrap=WORD)
source_txt.place(x=10,y=120,height=200,width=480)

list_text=list(LANGUAGES.values())

combo_source=ttk.Combobox(frame,value=list_text)
combo_source.place(x=10,y=350,height=40,width=150)
combo_source.set("English")

button_change=Button(frame,text="Translate",font=("Time new roman",10,"bold"),relief=RAISED,bg='gray',command=data)
button_change.place(x=175,y=350,height=40,width=150)

button_source_voice=Button(frame,text="voice",relief=RAISED,font=("Time new roman",10,"bold"),bg='gray',command=source_voice)
button_source_voice.place(x=430,y=325,height=20,width=60)


combo_destination=ttk.Combobox(frame,value=list_text)
combo_destination.place(x=340,y=350,height=40,width=150)
combo_destination.set("English")

leb_txt=Label(root,text="Destination Text:",font=("Time new roman",10,"bold"),fg='black',bg='white')
leb_txt.place(x=10,y=415,height=20,width=120)

destination_txt=Text(frame,font=("Time new roman",10,"bold"),wrap=WORD)
destination_txt.place(x=10,y=440,height=200,width=480)

button_destination_voice=Button(frame,text="voice",relief=RAISED,font=("Time new roman",10,"bold"),bg='gray',command=destination_voice)
button_destination_voice.place(x=430,y=645,height=20,width=60)


root.mainloop()