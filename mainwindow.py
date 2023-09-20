from tkinter import *
from pathlib import Path
from tkinter import font
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainWindow:
    def __init__(self, prevframe, frame, addframe, corpframe, viewframe, familyframe, deletedframe, add, viewall, family, corp):
        self.prevframe = prevframe
        self.frame = frame
        self.addframe = addframe
        self.corpframe = corpframe
        self.viewframe = viewframe
        self.familyframe = familyframe
        self.deletedframe = deletedframe
        self.add = add
        self.viewall = viewall
        self.family = family
        self.corp = corp
        self.frame.config(background="#FFFFFF")

        # Images
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.add_member_image = PhotoImage(file=relative_to_assets("addpage.png"))
        self.view_members_image = PhotoImage(file=relative_to_assets("viewallpage.png"))
        self.corp_image = PhotoImage(file=relative_to_assets("corporationpage.png"))
        self.family_image = PhotoImage(file=relative_to_assets("familypage.png"))
        self.deleted_image = PhotoImage(file=relative_to_assets("deletedpage.png"))
        self.backup_image = PhotoImage(file=relative_to_assets("backuppage.png"))
        self.header_image = PhotoImage(file=relative_to_assets("header.png"))

        # Fonts
        self.font2 = font.Font(family='Bold italic', size=12, weight='bold')

        # Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_greet())
        self.exit_btn.pack(pady=20)
        self.exit_btn.place(x=10, y=10)

        self.addmem_btn = Button(self.frame, image=self.add_member_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_add())
        self.addmem_btn.pack(pady=20)
        self.addmem_btn.place(x=170, y=149)

        self.corp_btn = Button(self.frame, image=self.corp_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_corp())
        self.corp_btn.pack(pady=20)
        self.corp_btn.place(x=647, y=291)

        self.view_btn = Button(self.frame, image=self.view_members_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_view())
        self.view_btn.pack(pady=20)
        self.view_btn.place(x=647, y=149)

        self.family_btn = Button(self.frame, image=self.family_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_family())
        self.family_btn.pack(pady=20)
        self.family_btn.place(x=170, y=291)

        self.deleted_btn = Button(self.frame, image=self.deleted_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_deleted())
        self.deleted_btn.pack(pady=20)
        self.deleted_btn.place(x=373, y=433)

        self.backup_btn = Button(self.frame, image=self.backup_image, relief='flat',borderwidth=0, highlightthickness=0)
        self.backup_btn.pack(pady=20)
        self.backup_btn.place(x=1023, y=560)

        self.header = Label(self.frame, image=self.header_image, bg='white', relief='flat',borderwidth=0, highlightthickness=0)
        self.header.pack()
        self.header.place(x=340, y=31)

    def change_to_greet(self):
        self.frame.pack_forget()
        self.prevframe.pack(fill="both",expand=True)

    def change_to_add(self):
        self.frame.pack_forget()
        self.addframe.pack(fill="both",expand=True)
        self.add.refresh_corps()

    def change_to_corp(self):
        self.frame.pack_forget()
        self.corpframe.pack(fill="both", expand=True)
        self.corp.refresh_corps()

    def change_to_view(self):
        self.frame.pack_forget()
        self.viewframe.pack(fill="both",expand=True)
        self.viewall.refresh_corps()

    def change_to_family(self):
        self.family.refresh()
        self.frame.pack_forget()
        self.familyframe.pack(fill="both",expand=True)

    def change_to_deleted(self):
        self.frame.pack_forget()
        self.deletedframe.pack(fill="both",expand=True)