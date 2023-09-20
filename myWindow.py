from tkinter import *
from database import *
from mainwindow import *
from greetwindow import *
from addmemwindow import *
from corpwindow import *
from viewallwindow import *
from familywindow import *
from deletedwindow import *
from query import *
from tkinter import font

class MyTkWindow:
    def __init__(self):
        self.main = Tk() #Makes the window
        self.main.wm_title("Window Title") #Makes the title that will appear in the top left
        self.main.config(background = "#FFFFFF")
        self.main.title("Magman's GYM Manager")
        self.main.geometry("1200x600")
        self.DB = DataBase()

        # Create the frames
        self.mainframe = Frame(self.main)
        self.greetframe = Frame(self.main)
        self.addframe = Frame(self.main)
        self.corpframe = Frame(self.main)
        self.viewframe = Frame(self.main)
        self.viewframe.config(bg="grey")
        self.familyframe = Frame(self.main)
        self.deletedframe = Frame(self.main)

        self.query = Query(self.main, self.viewframe, self.familyframe, self.corpframe, self.deletedframe, self.DB)
        self.corporations = []

        # Access the frames properties from other files
        self.greet = GreetWindow(self.mainframe, self.greetframe, self.DB)
        self.view = ViewAllWindow(self.mainframe, self.viewframe, self.query)
        self.add = AddMemWindow(self.mainframe, self.addframe, self.DB, self.main, self.query)
        self.corp = CorpWindow(self.mainframe, self.corpframe, self.query)
        self.family = FamilyWindow(self.mainframe, self.familyframe, self.query)
        self.delete = DeletedMemWindow(self.mainframe, self.deletedframe, self.query)
        self.mainwin = MainWindow(self.greetframe, self.mainframe, self.addframe, self.corpframe, self.viewframe,
                              self.familyframe, self.deletedframe, self.add, self.view, self.family, self.corp)

    def start(self):
        self.greetframe.pack(fill="both",expand=True)
        self.main.resizable(False, False)
        self.query.query_database()
        self.query.refresh_corps()
        self.main.mainloop() #start monitoring and updating the GUI