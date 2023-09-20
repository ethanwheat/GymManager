from tkinter import *
from tkinter import ttk
from pathlib import Path
from tkinter import font
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class FamilyWindow:
    def __init__(self, prevframe, frame, query):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.Query = query

        # Images
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.show_image = PhotoImage(file=relative_to_assets("showfamily.png"))
        self.renew_image = PhotoImage(file=relative_to_assets("renewfamily.png"))
        self.remove_image = PhotoImage(file=relative_to_assets("removefamily.png"))
        self.date_label = PhotoImage(file=relative_to_assets("datelabel.png"))
        self.family_label = PhotoImage(file=relative_to_assets("familylabel.png"))

        # Fonts
        self.font2 = font.Font(family='Bold italic', size=12, weight='bold')
        self.font3 = font.Font(family='Bold italic', size=17)
        self.small_font = font.Font(size=12)

        # Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_main())
        self.exit_btn.pack(pady=20)
        self.exit_btn.place(x=10, y=10)

        self.remove_btn = Button(self.frame, image=self.remove_image, relief='flat', borderwidth=0, highlightthickness=0, command=lambda: self.remove())
        self.remove_btn.pack(pady=20)
        self.remove_btn.place(x=200,y=427)

        self.renew_btn = Button(self.frame, image=self.renew_image, relief='flat', borderwidth=0, highlightthickness=0, command=lambda: self.renew())
        self.renew_btn.pack(pady=20)
        self.renew_btn.place(x=600,y=480)

        self.datelabel = Label(self.frame, image=self.date_label,bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.datelabel.pack()
        self.datelabel.place(x=600,y=427)

        self.familylabel = Label(self.frame, image=self.family_label, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.familylabel.pack()
        self.familylabel.place(x=523, y=11)

        self.renew_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.renew_entry.pack(pady=20)
        self.renew_entry.place(x=740, y=430)

        self.show_family = Button(self.frame, image= self.show_image, relief='flat', borderwidth=0, highlightthickness=0, command=self.add_famtree)
        self.show_family.pack(pady=20)
        self.show_family.place(x=200, y=480)

        self.family_box = Listbox(self.frame, height=16, width=25, borderwidth=2, relief='solid', font=self.small_font)
        self.family_box.pack(pady=20)
        self.family_box.place(x=90, y=70)

    def refresh(self):
        self.family_box.delete(0, END)
        for family in self.Query.families:
            self.family_box.insert(END, family)

    def remove(self):
        self.Query.remove_from_fam()
        self.refresh()

    def renew(self):
        selection = self.family_box.get(ANCHOR)
        self.Query.renew_family(selection, self.renew_entry.get().strip())
        self.renew_entry.delete(0, END)

    def add_famtree(self):
        selected = self.family_box.get(ANCHOR)
        self.Query.add_famtree(selected)

    def change_to_main(self):
        self.prevframe.pack(fill="both", expand=True)
        self.frame.pack_forget()
        for record in self.Query.family_tree.get_children():
            self.Query.family_tree.delete(record)
