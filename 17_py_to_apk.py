#file name should be main.py
from kivymd.app import MDapp
from kivymd.uix.label import MDLabel

class Main_App(MDapp):
    def build(self):
        return MDLabel(text="Welcome",halign="center")

if __name__=='__main__':
    Main_App().run()