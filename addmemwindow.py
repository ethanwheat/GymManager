from tkinter import *
from pathlib import Path
from tkinter import font
from tkinter import _setit
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from database import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AddMemWindow:
    def __init__(self, prevframe, frame, database, window, query):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.DB = database
        self.win = window
        self.Query = query

        # Fonts
        self.font2 = font.Font(family='Bold italic', size=12, weight='bold')
        self.font3 = font.Font(family='Bold italic', size=17)
        self.errorfont = font.Font(family='Bold italic', size=20)
        #self.label_font = font.Font(family='Helvetica',size=12)

        #Images
        self.addimage = PhotoImage(file=relative_to_assets("addmember.png"))
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.addmenu1 = PhotoImage(file=relative_to_assets("addmenu1.png"))
        self.addmenu2 = PhotoImage(file=relative_to_assets("addmenu2.png"))


        # Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_main())
        self.exit_btn.pack()
        self.exit_btn.place(x=10, y=10)

        self.add_btn = Button(self.frame, image=self.addimage, relief='flat',borderwidth=0, highlightthickness=0, font=self.font3, command=lambda: self.add_user())
        self.add_btn.pack(pady=20)
        self.add_btn.place(x=886, y=472)

        self.options1 = ["Month(s)", "Day(s)", "Year(s)"]
        self.options2 = ["Single", "Student", "Senior Citizen", "Military", "Family"]
        self.options3 = ["Yes", "No"]
        self.corporations = [""]

        # Labels
        self.data_entry1 = Label(self.frame, image=self.addmenu1, bg="white")
        self.data_entry1.pack()
        self.data_entry1.place(x=45, y=42)

        self.data_entry2 = Label(self.frame, image=self.addmenu2, bg="white")
        self.data_entry2.pack()
        self.data_entry2.place(x=58, y=434)

        self.error_label = Label(self.frame, text="", font=self.errorfont, bg="white", fg="red")
        self.error_label.pack(pady=20)
        self.error_label.place(x=315,y=525)

        self.fname_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.fname_entry.pack()
        self.fname_entry.place(x=320, y=50)
        self.lname_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9",font=self.font3, width=15)
        self.lname_entry.pack()
        self.lname_entry.place(x=320, y=149)
        self.card_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.card_entry.pack()
        self.card_entry.place(x=868, y=50)
        self.user_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.user_entry.pack()
        self.user_entry.place(x=868, y=149)
        self.phone_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.phone_entry.pack()
        self.phone_entry.place(x=320, y=248)
        self.today = date.today()

        self.date_print = (self.today.strftime('%m/%d/%Y'))
        self.start_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=15)
        self.start_entry.insert(-1, self.date_print)
        self.start_entry.pack()
        self.start_entry.place(x=320, y=350)
        self.menu1_value = StringVar()
        self.menu1_value.set("Month(s)")
        self.menu1 = OptionMenu(self.frame, self.menu1_value, *self.options1)
        self.menu1.config(width=12, font=self.font3,bg="#C9C9C9", relief='flat', borderwidth=0, highlightthickness=0)
        self.menu1.pack(pady=20)
        self.menu1.place(x=865, y=343)
        self.menu2_value = StringVar()
        self.menu2_value.set("Single")
        self.menu2 = OptionMenu(self.frame, self.menu2_value, *self.options2)
        self.menu2.config(width=12, font=self.font3, bg="#C9C9C9", relief='flat', borderwidth=0, highlightthickness=0)
        self.menu2.pack(pady=20)
        self.menu2.place(x=865, y=245)
        self.corp_value = StringVar()
        self.corp_value.set("N/A")
        self.corp_menu = OptionMenu(self.frame, self.corp_value, *self.corporations)
        self.corp_menu.config(width=12, font=self.font3, bg="#C9C9C9", relief='flat', borderwidth=0, highlightthickness=0)
        self.corp_menu.pack(pady=20)
        self.corp_menu.place(x=317, y=440)
        self.invoice_value = StringVar()
        self.invoice_value.set("No")
        self.invoicing = OptionMenu(self.frame, self.invoice_value, *self.options3)
        self.invoicing.config(width=6, font=self.font3, bg="#C9C9C9", relief='flat', borderwidth=0, highlightthickness=0)
        self.invoicing.pack(pady=20)
        self.invoicing.place(x=715, y=440)
        self.length_entry = Entry(self.frame, relief='flat', borderwidth=0, highlightthickness=0, bg="#C9C9C9", font=self.font3, width=3)
        self.length_entry.pack()
        self.length_entry.place(x=808, y=346)


    def change_to_main(self):
        self.prevframe.pack(fill="both",expand=True)
        self.frame.pack_forget()

    def make_label(self, root, text, x, y, font):
        my_label = Label(root, text=text, font=font)
        my_label.pack(pady=20)
        my_label.place(x=x, y=y)

    def get_date(self):
        today = date.today()
        dateprint = (today.strftime('%m/%d/%Y'))
        thedate = datetime.datetime.strptime(dateprint, "%m/%d/%Y")
        return thedate

    def add_user(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        cardnum = self.card_entry.get()
        usernum = self.user_entry.get()
        phonenum = self.phone_entry.get()
        startday = self.start_entry.get()
        length = self.length_entry.get()
        menu_1 = self.menu1_value.get()
        menu_2 = self.menu2_value.get()
        corp = self.corp_value.get()
        invoice = self.invoice_value.get()

        if len(fname.strip(" ")) > 0:
            if len(lname.strip(" ")) > 0:
                if len(phonenum.strip(" ")) > 0:
                    if len(cardnum.strip(" ")) > 0:
                        if len(usernum.strip(" ")) > 0:
                            if len(startday.strip(" ")) > 0:
                                if len(length.strip(" ")) > 0:
                                    try:
                                        date_1 = datetime.datetime.strptime(startday, "%m/%d/%Y")
                                        dateprint = (date_1.strftime('%m/%d/%Y'))
                                        if menu_1 == "Day(s)":
                                            new_date = (date_1 + datetime.timedelta(days=int(length)))
                                            exp_date = (new_date.strftime('%m/%d/%Y'))
                                        elif menu_1 == "Month(s)":
                                            new_date = date_1 + relativedelta(months=int(length))
                                            exp_date = (new_date.strftime('%m/%d/%Y'))
                                        elif menu_1 == "Year(s)":
                                            new_date = date_1 + relativedelta(years=int(length))
                                            exp_date = (new_date.strftime('%m/%d/%Y'))


                                        conn = self.DB.connect()
                                        c = conn.cursor()
                                        c.execute(
                                            "INSERT INTO members (last_name, first_name, card_num, user_num, phone_num, start_date, end_date, member_type, company, invoice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                            (
                                                lname, fname, cardnum, usernum, phonenum, dateprint, exp_date, menu_2, corp,
                                                invoice))
                                        self.DB.close_conection(conn, c)
                                        #if menu_2 == "Family":
                                            #refresh_family()
                                        self.fname_entry.delete(0, END)
                                        self.lname_entry.delete(0, END)
                                        self.card_entry.delete(0, END)
                                        self.user_entry.delete(0, END)
                                        self.phone_entry.delete(0, END)
                                        self.length_entry.delete(0, END)
                                        self.top = Toplevel(self.win)
                                        self.top.geometry("300x100")
                                        self.top.title("Success")
                                        self.make_label(self.top, "Member Added Successfully!", 20, 30, self.font3)
                                        self.menu1_value.set("Month(s)")
                                        self.menu2_value.set("Single")
                                        self.corp_value.set("N/A")
                                        self.invoice_value.set("No")
                                        self.Query.query_database()
                                        self.change_to_main()
                                    except:
                                        self.error_message("Start Day format should be mm/dd/yyyy")
                                else:
                                    self.error_message("Enter Membership Length")
                            else:
                                self.error_message("Enter a Start Day")
                        else:
                            self.error_message("Enter a User Number")
                    else:
                        self.error_message("Enter a Card Number")
                else:
                    self.error_message("Enter a Phone Number")
            else:
                self.error_message("Enter a Last Name")
        else:
            self.error_message("Enter a First Name")

    def refresh_corps(self):
        self.corp_menu['menu'].delete(0, 'end')
        for corpo in self.Query.corporations:
            self.corp_menu['menu'].add_command(label=corpo, command=_setit(self.corp_value, corpo))

    def error_message(self, msg):
        self.error_label['text'] = f'Error: {msg}'
        self.win.after(2000, self.clear_error)

    def clear_error(self):
        self.error_label['text'] = ""