from tkinter import *
from pathlib import Path
from tkinter import font

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CorpWindow:
    def __init__(self, prevframe, frame, query):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.Query = query

        # Images
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.show_image = PhotoImage(file=relative_to_assets("showcorp.png"))
        self.renew_image = PhotoImage(file=relative_to_assets("renewcorp.png"))
        self.remove_image = PhotoImage(file=relative_to_assets("removecorp.png"))
        self.name_label = PhotoImage(file=relative_to_assets("namelabel.png"))
        self.corp_label = PhotoImage(file=relative_to_assets("corplabel.png"))
        self.add_image = PhotoImage(file=relative_to_assets("addcorp.png"))
        self.delete_image = PhotoImage(file=relative_to_assets("deletecorp.png"))

        # Fonts
        self.font2 = font.Font(family='Bold italic', size=12, weight='bold')
        self.font3 = font.Font(family='Bold italic', size=17)
        self.small_font = font.Font(size=12)
        self.error_font = font.Font(family='Bold italic', size=20)

        # Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat', borderwidth=0, highlightthickness=0, command=lambda: self.change_to_main())
        self.exit_btn.pack(pady=20)
        self.exit_btn.place(x=10, y=10)

        self.Lb = Listbox(self.frame, height=16, width=25, font=self.small_font, borderwidth=2, relief='solid')
        self.Lb.pack(pady=20)
        self.Lb.place(x=65, y=70)

        self.corplabel = Label(self.frame, image=self.corp_label, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.corplabel.pack()
        self.corplabel.place(x=479,y=11)

        self.namelabel = Label(self.frame, image=self.name_label, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.namelabel.pack()
        self.namelabel.place(x=460,y=427)

        self.corpadd = Button(self.frame, image=self.add_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.add_corp())
        self.corpadd.pack(pady=20)
        self.corpadd.place(x=853, y=427)
        self.corpdel = Button(self.frame, image=self.delete_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.del_corp())
        self.corpdel.pack(pady=20)
        self.corpdel.place(x=81, y=480)
        self.corp_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.corp_entry.pack()
        self.corp_entry.place(x=640, y=430)

        self.employ_btn = Button(self.frame, image=self.show_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.corp_members())
        self.employ_btn.pack(pady=20)
        self.employ_btn.place(x=81, y=427)

        self.remove_btn = Button(self.frame, image=self.remove_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.remove_member())
        self.remove_btn.pack(pady=20)
        self.remove_btn.place(x=81, y=533)

        self.renew_btn = Button(self.frame, image=self.renew_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.renew_member())
        self.renew_btn.pack(pady=20)
        self.renew_btn.place(x=853, y=480)

        self.renew_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.renew_entry.pack(pady=20)
        self.renew_entry.place(x=640, y=483)

        self.error_label = Label(self.frame, textvariable=self.Query.error_msg, font=self.error_font, bg="white", fg="red")
        self.error_label.pack(pady=20)
        self.error_label.place(x=500,y=533)

    def add_corp(self):
        if len(self.corp_entry.get().strip()) > 2:
            if self.corp_entry.get().strip() not in self.Query.corporations:
                self.Lb.insert(self.Lb.size(), self.corp_entry.get().strip())
                self.Lb.config(height=self.Lb.size())
                f = open("corporations.txt", "a")
                f.write(self.corp_entry.get().strip() + "\n")
                f.close()
                self.corp_entry.delete(0, END)
            else:
                self.corp_entry.delete(0,END)
                self.Query.error_message("Error: Company Already Exists")
                return
        else:
            self.corp_entry.delete(0, END)
            self.Query.error_message("Error: Invalid Entry")
        self.Query.refresh_corps()
        self.Lb.config(height=16)

    def del_corp(self):
        try:
            linenum = self.Lb.curselection()[0] + 2
        except:
            self.Query.error_message("Error: No Selection Made")
            return
        f = open('corporations.txt', 'r')
        lines = f.readlines()
        ptr = 1
        fw = open('corporations.txt', 'w')
        for line in lines:
            if ptr != linenum:
                fw.write(line)
            ptr += 1
        f.close()
        fw.close()
        self.Lb.delete(self.Lb.curselection())
        self.Lb.config(height=16)
        self.Query.refresh_corps()

    def corp_members(self):
        try:
            linenum = self.Lb.curselection()[0] + 2
        except:
            self.Query.error_message("Error: No Selection Made")
            return
        entry = self.Lb.get(ANCHOR)
        for record in self.Query.corp_tree.get_children():
            self.Query.corp_tree.delete(record)
        conn = self.Query.DB.connect()
        c = conn.cursor()
        c.execute("SELECT * FROM members")
        records = c.fetchall()
        for record in records:
            if str(entry.strip()) == str(record[8].strip()):
                self.Query.corp_tree.insert(parent='', index='end', text='',
                                 values=(
                                     record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                 tags=('rowstyle',))
        self.Query.DB.close_conection(conn, c)

    def remove_member(self):
        self.Query.remove_from_corp()

    def renew_member(self):
        date = self.renew_entry.get().strip()
        self.Query.renew_corp(date)
        self.renew_entry.delete(0,END)

    def refresh_corps(self):
        self.Lb.delete(0, END)
        for corpo in self.Query.corporations:
            if corpo != "N/A":
                self.Lb.insert(END, corpo)

    def change_to_main(self):
        self.prevframe.pack(fill="both", expand=True)
        self.frame.pack_forget()
        for record in self.Query.corp_tree.get_children():
            self.Query.corp_tree.delete(record)
