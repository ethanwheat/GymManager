from tkinter import *
from tkinter import font
import datetime
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DeletedMemWindow:
    def __init__(self, prevframe, frame, query):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.Query = query

        #Fonts
        self.font3 = font.Font(family='Bold italic', size=17)

        #Images
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.renew_image = PhotoImage(file=relative_to_assets("renewdeleted.png"))
        self.remove_image = PhotoImage(file=relative_to_assets("removedeleted.png"))
        self.date_label = PhotoImage(file=relative_to_assets("renewlabel.png"))
        self.deleted_label = PhotoImage(file=relative_to_assets("deletedlabel.png"))
        self.confirm_image = PhotoImage(file=relative_to_assets("confirmdeleted.png"))
        self.cancel_image = PhotoImage(file=relative_to_assets("canceldeleted.png"))

        #Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_main())
        self.exit_btn.pack(pady=20)
        self.exit_btn.place(x=10, y=10)

        self.remove_btn = Button(self.frame, image=self.remove_image, relief='flat', borderwidth=0, highlightthickness=0, command=lambda: self.remove())
        self.remove_btn.pack(pady=20)
        self.remove_btn.place(x=634,y=427)

        self.renew_btn = Button(self.frame, image=self.renew_image, relief='flat', borderwidth=0, highlightthickness=0, command=lambda: self.renew())
        self.renew_btn.pack(pady=20)
        self.renew_btn.place(x=260,y=427)
        self.cancel_btn = Button(self.frame)
        self.cancel_btn.destroy()

        self.deletedlabel = Label(self.frame, image=self.deleted_label, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.deletedlabel.pack()
        self.deletedlabel.place(x=439, y=11)

    def change_to_main(self):
        self.prevframe.pack(fill="both", expand=True)
        self.frame.pack_forget()
        if self.cancel_btn.winfo_exists():
            self.cancel()

    def remove(self):
        try:
            self.cancel_remove()
        except:
            pass
        self.cancel_remove_btn = Button(self.frame, image=self.cancel_image, relief='flat', borderwidth=0, highlightthickness=0, command=self.cancel_remove)
        self.cancel_remove_btn.pack()
        self.cancel_remove_btn.place(x=464, y=500)
        self.confirm_remove_btn = Button(self.frame, image=self.confirm_image, relief='flat', borderwidth=0, highlightthickness=0, command=self.confirm_remove)
        self.confirm_remove_btn.pack()
        self.confirm_remove_btn.place(x=626, y=500)
        try:
            self.cancel()
        except:
            return

    def renew(self):
        try:
            self.cancel()
        except:
            pass
        self.cancel_btn = Button(self.frame, image=self.cancel_image, relief='flat', borderwidth=0, highlightthickness=0, command=self.cancel)
        self.cancel_btn.pack()
        self.cancel_btn.place(x=165, y=500)
        self.renew_label = Label(self.frame, image=self.date_label, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.renew_label.pack()
        self.renew_label.place(x=300, y=500)
        self.renew_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.renew_entry.pack()
        self.renew_entry.place(x=715, y=503)
        self.renew_confirm = Button(self.frame, image=self.confirm_image, relief='flat', borderwidth=0, highlightthickness=0, command=self.confirm)
        self.renew_confirm.pack()
        self.renew_confirm.place(x=924, y=500)
        try:
            self.cancel_remove()
        except:
            return

    def cancel(self):
        self.cancel_btn.destroy()
        self.renew_label.destroy()
        self.renew_entry.destroy()
        self.renew_confirm.destroy()

    def cancel_remove(self):
        self.cancel_remove_btn.destroy()
        self.confirm_remove_btn.destroy()

    def confirm(self):
        date = self.renew_entry.get().strip()
        self.Query.renew(date)
        self.cancel()

    def confirm_remove(self):
        self.Query.remove()
        self.cancel_remove()