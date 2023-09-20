from tkinter import *
from pathlib import Path
from tkinter import font
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class GreetWindow:
    def __init__(self, prevframe, frame, db):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.database = db
        # Images
        self.tkimage = PhotoImage(file=relative_to_assets("button_1.png"))
        self.tkimage2 = PhotoImage(file=relative_to_assets("image_3.png"))

        # Fonts
        self.font1 = font.Font(family='Abel', size=22)

        self.password_label = Label(self.frame, image=self.tkimage2, bg="white")
        self.password_label.pack()
        self.password_entry = Entry(self.frame, font=self.font1, bg="#c9c9c9", show="*", borderwidth=3, highlightthickness=0,
                               relief="flat")
        self.password_entry.pack(pady=40)
        self.confirm_btn = Button(self.frame, image=self.tkimage, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: self.password())
        self.confirm_btn.pack()

    def change_to_greet(self):
        self.frame.pack(fill="both",expand=True)
        self.prevframe.pack_forget()

    def change_to_order(self):
        self.prevframe.pack(fill="both",expand=True)
        self.frame.pack_forget()

    def password(self):
        if self.password_entry.get() == self.database.login:
            self.change_to_order()
            self.password_entry.delete(0, END)