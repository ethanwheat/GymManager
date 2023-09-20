from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime
from datetime import *

class Query:
    def __init__(self, window, viewall, family, corp, deleted, DB):
        self.DB = DB
        self.win = window

        #Error Messages
        self.error_font = font.Font(family='Bold italic', size=20)
        self.error_msg = StringVar()
        self.error_msg.set("")

        self.error_view = Label(viewall, textvariable=self.error_msg, font=self.error_font, bg="white", fg="red")
        self.error_view.pack(pady=20)
        self.error_view.place(x=745, y=545)

        self.error_deleted = Label(deleted, textvariable=self.error_msg, font=self.error_font, bg="white", fg="red")
        self.error_deleted.pack(pady=20)
        self.error_deleted.place(x=450,y=550)

        self.error_fam = Label(family, textvariable=self.error_msg, font=self.error_font, bg="white", fg="red")
        self.error_fam.pack(pady=20)
        self.error_fam.place(x=400,y=525)

        self.style = ttk.Style()
        # Pick A Theme
        self.style.theme_use('default')
        self.font3 = font.Font(family='Bold italic', size=10)
        # Configure the Treeview Colors
        self.style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white",
                        highlightthickness=1,
                        borderwidth=2,
                        relief='flat',
                        font=self.font3)

        # Change Selected Color
        self.style.map('Treeview', background=[('selected', "#347083")])

        self.member_frame = Frame(viewall)
        self.member_frame.config(background="#FFFFFF")
        self.member_frame.pack(fill='both',expand=True)
        self.member_frame.place(x=20, y=50)
        # Create a Treeview Scrollbar
        self.member_scroll = Scrollbar(self.member_frame)
        self.member_scroll.pack(side=RIGHT, fill=Y)
        # Create The Treeview
        self.member_tree = ttk.Treeview(self.member_frame, yscrollcommand=self.member_scroll.set, selectmode="extended")
        self.member_tree.pack(pady=20)

        # Configure the Scrollbar
        self.member_scroll.config(command=self.member_tree.yview)

        # Define Our Columns
        self.member_tree['columns'] = ("Last Name", "First Name", "Card #", "User #", "Phone #", "Start Day", "End Day",
                                       "Type", "Invoice", "Corporation")

        # Format Our Columns
        self.member_tree.column("#0", width=0, stretch=NO)
        self.member_tree.column("Last Name", anchor=W, width=160)
        self.member_tree.column("First Name", anchor=W, width=160)
        self.member_tree.column("Card #", anchor=CENTER, width=80)
        self.member_tree.column("User #", anchor=CENTER, width=80)
        self.member_tree.column("Phone #", anchor=CENTER, width=120)
        self.member_tree.column("Start Day", anchor=CENTER, width=100)
        self.member_tree.column("End Day", anchor=CENTER, width=100)
        self.member_tree.column("Type", anchor=CENTER, width=140)
        self.member_tree.column("Invoice", anchor=CENTER, width=80)
        self.member_tree.column("Corporation", anchor=CENTER, width=140)

        # Create Headings
        self.member_tree.heading("#0", text="", anchor=W)
        self.member_tree.heading("Last Name", text="Last Name", anchor=W,
                        command=lambda: self.treeview_sort_column(self.member_tree, "0", True))
        self.member_tree.heading("First Name", text="First Name", anchor=W,
                        command=lambda: self.treeview_sort_column(self.member_tree, "1", True))
        self.member_tree.heading("Card #", text="Card #", anchor=CENTER)
        self.member_tree.heading("User #", text="User #", anchor=CENTER)
        self.member_tree.heading("Phone #", text="Phone #", anchor=CENTER)
        self.member_tree.heading("Start Day", text="Start Day", anchor=CENTER)
        self.member_tree.heading("End Day", text="End Day", anchor=CENTER)
        self.member_tree.heading("Type", text="Type", anchor=CENTER)
        self.member_tree.heading("Invoice", text="Invoice", anchor=CENTER,
                        command=lambda: self.treeview_sort_column(self.member_tree, "8", True))
        self.member_tree.heading("Corporation", text="Corporation", anchor=CENTER,
                        command=lambda: self.treeview_sort_column(self.member_tree, "9", True))
        self.member_tree.heading("#0", command=lambda: self.treeview_sort_column(self.member_tree, "#0", False))

        self.member_tree.tag_configure('rowstyle', background="white")

        ###############
        # Family Tree #
        ###############

        self.families = []

        self.family_frame = Frame(family)
        self.family_frame.config(background="#FFFFFF")
        self.family_frame.pack()
        self.family_frame.place(x=400, y=50)

        self.family_scroll = Scrollbar(self.family_frame)
        self.family_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        self.family_tree = ttk.Treeview(self.family_frame, yscrollcommand=self.family_scroll.set, selectmode="extended")
        self.family_tree.pack(pady=20)

        # Configure the Scrollbar
        self.family_scroll.config(command=self.family_tree.yview)

        # Define Our Columns
        self.family_tree['columns'] = ("Last Name", "First Name", "Card #", "User #", "Phone #", "Start Day", "End Day")

        # Format Our Columns
        self.family_tree.column("#0", width=0, stretch=NO)
        self.family_tree.column("Last Name", anchor=W, width=140)
        self.family_tree.column("First Name", anchor=W, width=140)
        self.family_tree.column("Card #", anchor=CENTER, width=60)
        self.family_tree.column("User #", anchor=CENTER, width=60)
        self.family_tree.column("Phone #", anchor=CENTER, width=100)
        self.family_tree.column("Start Day", anchor=CENTER, width=80)
        self.family_tree.column("End Day", anchor=CENTER, width=80)

        # Create Headings
        self.family_tree.heading("#0", text="", anchor=W)
        self.family_tree.heading("Last Name", text="Last Name", anchor=W,
                            command=lambda: self.treeview_sort_column(self.family_tree, "0", True))
        self.family_tree.heading("First Name", text="First Name", anchor=W,
                            command=lambda: self.treeview_sort_column(self.family_tree, "1", True))
        self.family_tree.heading("Card #", text="Card #", anchor=CENTER)
        self.family_tree.heading("User #", text="User #", anchor=CENTER)
        self.family_tree.heading("Phone #", text="Phone #", anchor=CENTER)
        self.family_tree.heading("Start Day", text="Start Day", anchor=CENTER)
        self.family_tree.heading("End Day", text="End Day", anchor=CENTER)
        self.family_tree.heading("#0", command=lambda: self.treeview_sort_column(self.family_tree, "#0", False))

        self.family_tree.tag_configure('rowstyle', background="white")

        ##############
        # Corpo Tree #
        ##############

        self.corporations = []

        self.corp_frame = Frame(corp)
        self.corp_frame.config(background="#FFFFFF")
        self.corp_frame.pack()
        self.corp_frame.place(x=400, y=50)
        # Create a Treeview Scrollbar
        self.corp_scroll = Scrollbar(self.corp_frame)
        self.corp_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        self.corp_tree = ttk.Treeview(self.corp_frame, yscrollcommand=self.corp_scroll.set, selectmode="extended")
        self.corp_tree.pack(pady=20)

        # Configure the Scrollbar
        self.corp_scroll.config(command=self.corp_tree.yview)

        # Configure the Scrollbar
        self.corp_scroll.config(command=self.corp_tree.yview)

        # Define Our Columns
        self.corp_tree['columns'] = ("Last Name", "First Name", "Card #", "User #", "Phone #", "Start Day", "End Day")

        # Format Our Columns
        self.corp_tree.column("#0", width=0, stretch=NO)
        self.corp_tree.column("Last Name", anchor=W, width=140)
        self.corp_tree.column("First Name", anchor=W, width=140)
        self.corp_tree.column("Card #", anchor=CENTER, width=60)
        self.corp_tree.column("User #", anchor=CENTER, width=60)
        self.corp_tree.column("Phone #", anchor=CENTER, width=100)
        self.corp_tree.column("Start Day", anchor=CENTER, width=80)
        self.corp_tree.column("End Day", anchor=CENTER, width=80)

        # Create Headings
        self.corp_tree.heading("#0", text="", anchor=W)
        self.corp_tree.heading("Last Name", text="Last Name", anchor=W,
                          command=lambda: self.treeview_sort_column(self.corp_tree, "0", True))
        self.corp_tree.heading("First Name", text="First Name", anchor=W,
                          command=lambda: self.treeview_sort_column(self.corp_tree, "1", True))
        self.corp_tree.heading("Card #", text="Card #", anchor=CENTER)
        self.corp_tree.heading("User #", text="User #", anchor=CENTER)
        self.corp_tree.heading("Phone #", text="Phone #", anchor=CENTER)
        self.corp_tree.heading("Start Day", text="Start Day", anchor=CENTER)
        self.corp_tree.heading("End Day", text="End Day", anchor=CENTER)
        self.corp_tree.heading("#0", command=lambda: self.treeview_sort_column(self.corp_tree, "#0", False))

        self.corp_tree.tag_configure('rowstyle', background="white")

        ################
        # Deleted Tree #
        ################

        self.corporations = []

        self.deleted_frame = Frame(deleted)
        self.deleted_frame.config(background="#FFFFFF")
        self.deleted_frame.pack()
        self.deleted_frame.place(x=20, y=50)
        # Create a Treeview Scrollbar
        self.deleted_scroll = Scrollbar(self.deleted_frame)
        self.deleted_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        self.deleted_tree = ttk.Treeview(self.deleted_frame, yscrollcommand=self.deleted_scroll.set, selectmode="extended")
        self.deleted_tree.pack(pady=20)

        # Configure the Scrollbar
        self.deleted_scroll.config(command=self.deleted_tree.yview)

        # Configure the Scrollbar
        self.deleted_scroll.config(command=self.deleted_tree.yview)

        # Define Our Columns
        self.deleted_tree['columns'] = ("Last Name", "First Name", "Card #", "User #", "Phone #", "Start Day", "End Day",
                                       "Type", "Invoice", "Corporation")

        # Format Our Columns
        self.deleted_tree.column("#0", width=0, stretch=NO)
        self.deleted_tree.column("Last Name", anchor=W, width=160)
        self.deleted_tree.column("First Name", anchor=W, width=160)
        self.deleted_tree.column("Card #", anchor=CENTER, width=80)
        self.deleted_tree.column("User #", anchor=CENTER, width=80)
        self.deleted_tree.column("Phone #", anchor=CENTER, width=120)
        self.deleted_tree.column("Start Day", anchor=CENTER, width=100)
        self.deleted_tree.column("End Day", anchor=CENTER, width=100)
        self.deleted_tree.column("Type", anchor=CENTER, width=140)
        self.deleted_tree.column("Invoice", anchor=CENTER, width=80)
        self.deleted_tree.column("Corporation", anchor=CENTER, width=140)

        # Create Headings
        self.deleted_tree.heading("#0", text="", anchor=W)
        self.deleted_tree.heading("Last Name", text="Last Name", anchor=W,
                          command=lambda: self.treeview_sort_column(self.deleted_tree, "0", True))
        self.deleted_tree.heading("First Name", text="First Name", anchor=W,
                          command=lambda: self.treeview_sort_column(self.deleted_tree, "1", True))
        self.deleted_tree.heading("Card #", text="Card #", anchor=CENTER)
        self.deleted_tree.heading("User #", text="User #", anchor=CENTER)
        self.deleted_tree.heading("Phone #", text="Phone #", anchor=CENTER)
        self.deleted_tree.heading("Start Day", text="Start Day", anchor=CENTER)
        self.deleted_tree.heading("End Day", text="End Day", anchor=CENTER)
        self.deleted_tree.heading("#0", command=lambda: self.treeview_sort_column(self.deleted_tree, "#0", False))
        self.deleted_tree.heading("Type", text="Type", anchor=CENTER)
        self.deleted_tree.heading("Invoice", text="Invoice", anchor=CENTER,
                        command=lambda: self.treeview_sort_column(self.deleted_tree, "8", True))
        self.deleted_tree.heading("Corporation", text="Corporation", anchor=CENTER,
                        command=lambda: self.treeview_sort_column(self.deleted_tree, "9", True))
        self.deleted_tree.heading("#0", command=lambda: self.treeview_sort_column(self.deleted_tree, "#0", False))

        self.deleted_tree.tag_configure('rowstyle', background="white")

    def tree_value(self):
        selected = self.member_tree.focus()
        values = self.member_tree.item(selected, 'values')
        return values

    def get_date(self):
        today = date.today()
        dateprint = (today.strftime('%m/%d/%Y'))
        thedate = datetime.strptime(dateprint, "%m/%d/%Y")
        return thedate

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=not reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def query_database(self):
        # Clear the Treeview
        for record in self.member_tree.get_children():
            self.member_tree.delete(record)
        for record in self.deleted_tree.get_children():
            self.deleted_tree.delete(record)

        # Create a database or connect to one that exists
        conn = self.DB.connect()
        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT * FROM members")
        records = c.fetchall()

        family_list = []
        for record in records:
            if record[6].strip() != "Deleted":
                self.member_tree.insert(parent='', index='end', text='',
                            values=(
                            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[9], record[8]),
                            tags=('rowstyle',))
            else:
                self.deleted_tree.insert(parent='', index='end', text='',
                            values=(
                            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[9], record[8]),
                            tags=('rowstyle',))
            if "Family" == record[7]:
                    family_list.append(record[0])
        self.families = [*set(family_list)]
        #treeview_sort_column(self.member_tree, "0", True)
        self.DB.close_conection(conn, c)

    def search_expired(self):
        for record in self.member_tree.get_children():
            self.member_tree.delete(record)
        conn = self.DB.connect()
        c = conn.cursor()
        c.execute("SELECT * FROM members")
        records = c.fetchall()

        dates = []
        for record in records:
            if record[6].strip() != "Deleted":
                tempdate = datetime.strptime(record[6].replace(" ", ""), "%m/%d/%Y")
                remaining = tempdate - self.get_date()
                if remaining < timedelta(days=5):
                    time_left = str(remaining)
                    time_left = time_left.replace(":", "  ")
                    time_left = time_left.split()
                    days_left = int(time_left[0])
                    if days_left == 0:
                        self.member_tree.insert(parent='', index='end', text='',
                                       values=(
                                       record[0], record[1], record[2], record[3], record[4], record[5],
                                       "Expired Today",
                                       record[7],
                                       record[9], record[8]),
                                       tags=('rowstyle',))
                    elif days_left < 0:
                        days_left = str(days_left).strip("-")
                        self.member_tree.insert(parent='', index='end', text='',
                                   values=(record[0], record[1], record[2], record[3], record[4], record[5],
                                           days_left + " days ago", record[7], record[9], record[8]),
                                       tags=('rowstyle',))
                    elif days_left > 0:
                        days_left = str(days_left).strip("-")
                        self.member_tree.insert(parent='', index='end', text='',
                                   values=(
                                           record[0], record[1], record[2], record[3], record[4], record[5],
                                           "in " + days_left + " days",
                                           record[7],
                                           record[9], record[8]),
                                    tags=('rowstyle',))
        self.DB.close_conection(conn, c)

    def search_members(self, num, entry):

        for record in self.member_tree.get_children():
            self.member_tree.delete(record)

        # Create a database or connect to one that exists
        conn = self.DB.connect()
        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT * FROM members")
        records = c.fetchall()

        for record in records:
            if entry.lower() in str(record[num]).lower():
                self.member_tree.insert(parent='', index='end', text='',
                               values=(
                                   record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                   record[7],
                                   record[9], record[8]),
                               tags=('rowstyle',))
        self.DB.close_conection(conn, c)

    def update_record(self, entries):
        x = self.member_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        try:
            valid = datetime.strptime(entries[6], "%m/%d/%Y")
        except:
            self.error_message("Invalid Date (MM/DD/YYYY)")
            return
        selected = self.member_tree.focus()
        values = self.member_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                   SET last_name=%s, first_name=%s, card_num=%s, user_num=%s, phone_num=%s, start_date=%s, end_date=%s, member_type=%s, company=%s, invoice=%s 
                   WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s'''
        value = (entries + (values[1], values[0], values[2], values[3]))
        c.execute(query, value)

        if entries[7] == "Family":
            self.families.append(entries[0])
            self.families = [*set(self.families)]

        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()

    def renew(self, date):
        x = self.deleted_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        try:
            valid = datetime.strptime(date, "%m/%d/%Y")
        except:
            self.error_message("Invalid Date (MM/DD/YYYY)")
            return
        selected = self.deleted_tree.focus()
        values = self.deleted_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                   SET end_date=%s
                   WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
        value = [date, values[1], values[0], values[2], values[3], values[5]]
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn,c)
        self.query_database()

    def renew_corp(self, renew_date):
        x = self.corp_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        try:
            valid = datetime.strptime(renew_date, "%m/%d/%Y")
        except:
            self.error_message("Invalid Date (MM/DD/YYYY)")
            return
        selected = self.corp_tree.focus()
        values = self.corp_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                           SET end_date=%s
                           WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
        value = [renew_date, values[1], values[0], values[2], values[3], values[5]]
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()
        for record in self.corp_tree.get_children():
            self.corp_tree.delete(record)

    def renew_family(self, family, renew_date):
        if len(family) == 0:
            self.error_message("Error: No Selection Made")
            return
        try:
            valid = datetime.strptime(renew_date, "%m/%d/%Y")
        except:
            self.error_message("Invalid Date (MM/DD/YYYY)")
            return
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                                   SET end_date=%s
                                   WHERE last_name=%s AND member_type=%s'''
        value = [renew_date, family, "Family"]
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()
        for record in self.family_tree.get_children():
            self.family_tree.delete(record)


    def delete(self):
        x = self.member_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        selected = self.member_tree.focus()
        values = self.member_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                           SET end_date=%s
                           WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
        value = ("Deleted", values[1], values[0], values[2], values[3], values[5])
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()

    def remove(self):
        x = self.deleted_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        selected = self.deleted_tree.focus()
        values = self.deleted_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        c.execute("DELETE from members WHERE first_name = %s and last_name = %s and card_num = %s and user_num = %s and start_date=%s",
                  (values[1], values[0], values[2], values[3], values[5]))
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()

    def remove_from_corp(self):
        x = self.corp_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        selected = self.corp_tree.focus()
        values = self.corp_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        query = '''UPDATE members 
                                   SET company=%s
                                   WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
        value = ("N/A", values[1], values[0], values[2], values[3], values[5])
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()
        for record in self.corp_tree.get_children():
            self.corp_tree.delete(record)

    def remove_from_fam(self):
        x = self.family_tree.selection()
        if len(x) == 0:
            self.error_message("Error: No Selection Made")
            return
        selected = self.family_tree.focus()
        values = self.family_tree.item(selected, 'values')
        conn = self.DB.connect()
        c = conn.cursor()
        if "-" in values[1]:
            name = values[1].split("-")
            query = '''UPDATE members 
                                   SET last_name=%s, first_name=%s, member_type=%s
                                   WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
            value = (name[1], name[0], "Single", values[1], values[0], values[2], values[3], values[5])
        else:
            query = '''UPDATE members 
                                   SET member_type=%s
                                   WHERE first_name=%s AND last_name=%s AND card_num=%s AND user_num=%s AND start_date=%s'''
            value = ("Single", values[1], values[0], values[2], values[3], values[5])
        c.execute(query, value)
        conn.commit()
        self.DB.close_conection(conn, c)
        self.query_database()
        for record in self.family_tree.get_children():
            self.family_tree.delete(record)

    def add_famtree(self, selected):
        if len(selected) == 0:
            self.error_message("Error: No Selection Made")
            return
        for record in self.family_tree.get_children():
            self.family_tree.delete(record)

        conn = self.DB.connect()
        c = conn.cursor()

        c.execute("SELECT * FROM members")
        records = c.fetchall()

        for record in records:
            if selected == record[0] and record[7] == "Family":
                self.family_tree.insert(parent='', index='end', text='',
                                   values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                   tags=('rowstyle',))
        self.DB.close_conection(conn, c)

    def refresh_corps(self):
        corplist = []
        corps = open("corporations.txt", "r")
        for comp in corps:
            if comp not in corplist:
                corplist.append(comp.strip())
        corps.close()
        self.corporations = corplist

    def error_message(self, msg):
        self.error_msg.set(msg)
        self.win.update()
        self.win.after(2000, self.clear_error())

    def clear_error(self):
        self.error_msg.set("")
