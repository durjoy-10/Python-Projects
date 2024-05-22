import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files():
    path = folder_path.get()
    files = os.listdir(path)
    
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            filename, extension = os.path.splitext(file)
            extension_1 = extension[1:]
            folder_path_new = os.path.join(path, extension_1)
            
            if not os.path.exists(folder_path_new):
                os.makedirs(folder_path_new)
                
            shutil.move(os.path.join(path, file), os.path.join(folder_path_new, file))
    
    status_label.config(text="Files organized successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# Create the main application window
fm = tk.Tk()
fm.title("File Organizer")
fm.config(bg='white')
fm.geometry('500x250')

#creating a Label 
Title_label=tk.Label(fm,text="FILE MANAGEMENT SYSTEM",font=('Times New Roman',17,'bold'),bg='blue',fg='white')
Title_label.place(x=25,y=20,height=50,width=450)

# Create a label and entry for folder path
folder_path = tk.StringVar()
# folder_path_label = tk.Label(fm, text="Select a folder",font=('Times New Roman',17,'bold'))
# folder_path_label.place(x=150,y=80,height=30,width=200)

folder_entry = tk.Entry(fm, textvariable=folder_path,bg='purple')
folder_entry.place(x=150,y=80,height=30,width=200)

# Create a button to browse folders
browse_button = tk.Button(fm, text="Select a folder",font=('Times New Roman',17,'bold'),bg='yellow', command=browse_folder)
browse_button.place(x=150,y=120,height=30,width=200)

# Create a button to organize files
organize_button = tk.Button(fm, text="Organize Files",font=('Times New Roman',17,'bold'),bg='orange',command=organize_files)
organize_button.place(x=150,y=160,height=30,width=200)

# Create a status label
status_label = tk.Label(fm, text="",bg='white',fg='green')
status_label.place(x=150,y=200,height=30,width=200)

# Run the Tkinter event loop
fm.mainloop()
