from tkinter import *
from pathlib import Path
from tkinter import font
from tkinter import _setit
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ViewAllWindow:
    def __init__(self, prevframe, frame, query):
        self.prevframe = prevframe
        self.frame = frame
        self.frame.config(background="#FFFFFF")
        self.Query = query

        self.options_search = ['Last Name', 'First Name', 'Card Number', 'User Number', 'Phone Number',
                          'Expired/Expiring Soon']

        # Images
        self.exit_image = PhotoImage(file=relative_to_assets("exitbutton.png"))
        self.search_bar_image = PhotoImage(file=relative_to_assets("searchbar.png"))
        self.search_button_image = PhotoImage(file=relative_to_assets("searchbutton.png"))
        self.refresh_button_image = PhotoImage(file=relative_to_assets("refreshbutton.png"))
        self.update_button_image = PhotoImage(file=relative_to_assets("updatebutton.png"))
        self.delete_button_image = PhotoImage(file=relative_to_assets("deletebutton.png"))
        self.family_button_image = PhotoImage(file=relative_to_assets("familybutton.png"))

        # Fonts
        self.font2 = font.Font(family='Bold italic', size=12)
        self.font3 = font.Font(family='Bold italic', size=14)

        self.options1 = ["Month(s)", "Day(s)", "Year(s)"]
        self.options2 = ["Single", "Student", "Senior Citizen", "Military", "Family"]
        self.options3 = ["Yes", "No"]

        self.corporations = [""]
        self.corp_value = StringVar()
        self.corp_value.set("N/A")

        self.invoice_value = StringVar()
        self.invoice_value.set("No")

        self.menu2_value = StringVar()
        self.menu2_value.set("Single")

        self.search_bar = Label(self.frame, image=self.search_bar_image, bg="white")
        self.search_bar.pack(pady=20)
        self.search_bar.place(x=350, y=5)

        # Buttons
        self.exit_btn = Button(self.frame, image=self.exit_image, relief='flat',borderwidth=0, highlightthickness=0, command=lambda: self.change_to_main())
        self.exit_btn.pack(pady=20)
        self.exit_btn.place(x=10, y=10)

        self.search_value = StringVar()
        self.search_value.set("Last Name")
        self.search_menu = OptionMenu(self.frame, self.search_value, *self.options_search)
        self.search_menu.config(width=17, font=self.font2, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.search_menu.pack(pady=20)
        self.search_menu.place(x=557, y=14)

        self.search_entry = Entry(self.frame, font=self.font3, width=17, relief='flat', borderwidth=0, highlightthickness=0)
        self.search_entry.pack()
        self.search_entry.place(x=357, y=14)

        self.search_btn = Button(self.frame, image=self.search_button_image, command=self.search)
        self.search_btn.config(relief='flat', borderwidth=0, highlightthickness=0)
        self.search_btn.pack(pady=20)
        self.search_btn.place(x=760, y=7)

        self.frame_btn = Button(self.frame, image=self.refresh_button_image, bg="white", relief='flat', borderwidth=0, highlightthickness=0,
                             command=lambda: [self.Query.query_database(), self.clear_entries()])
        self.frame_btn.pack(pady=20)
        self.frame_btn.place(x=1080, y=10)

        self.update_btn = Button(self.frame, image=self.update_button_image, bg="white", relief='flat', borderwidth=0, highlightthickness=0, command=self.update)
        self.update_btn.pack(pady=20)
        self.update_btn.place(x=50, y=550)

        self.family_btn = Button(self.frame, image=self.family_button_image, bg="white", relief='flat', borderwidth=0, highlightthickness=0)
        self.family_btn.pack(pady=20)
        self.family_btn.place(x=510, y=550)

        self.delete_btn = Button(self.frame, image=self.delete_button_image, bg="white", relief='flat', borderwidth=0, highlightthickness=0, command=self.delete)
        self.delete_btn.pack(pady=20)
        self.delete_btn.place(x=280, y=550)

        self.data_frame = LabelFrame(self.frame, text="Selected Record")
        self.data_frame.config(bg="White")
        self.data_frame.pack(fill="x", expand="yes", padx=20)
        self.data_frame.place(x=50, y=420)

        self.fn_label = Label(self.data_frame, text="First Name")
        self.fn_label.grid(row=0, column=0, padx=10, pady=10)
        self.fn_entry = Entry(self.data_frame)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10)

        self.ln_label = Label(self.data_frame, text="Last Name")
        self.ln_label.grid(row=0, column=2, padx=10, pady=10)
        self.ln_entry = Entry(self.data_frame)
        self.ln_entry.grid(row=0, column=3, padx=10, pady=10)

        self.card_label = Label(self.data_frame, text="Card #")
        self.card_label.grid(row=0, column=4, padx=10, pady=10)
        self.cardnum_entry = Entry(self.data_frame)
        self.cardnum_entry.grid(row=0, column=5, padx=10, pady=10)

        self.user_label = Label(self.data_frame, text="User #")
        self.user_label.grid(row=0, column=6, padx=10, pady=10)
        self.usernum_entry = Entry(self.data_frame)
        self.usernum_entry.grid(row=0, column=7, padx=10, pady=10)

        self.phone_label = Label(self.data_frame, text="Phone #")
        self.phone_label.grid(row=0, column=8, padx=10, pady=10)
        self.phonenum_entry = Entry(self.data_frame)
        self.phonenum_entry.grid(row=0, column=9, padx=10, pady=10)

        self.start_label = Label(self.data_frame, text="Start Day")
        self.start_label.grid(row=1, column=0, padx=10, pady=10)
        self.startday_entry = Entry(self.data_frame)
        self.startday_entry.grid(row=1, column=1, padx=10, pady=10)

        self.end_label = Label(self.data_frame, text="End Day")
        self.end_label.grid(row=1, column=2, padx=10, pady=10)
        self.end_entry = Entry(self.data_frame)
        self.end_entry.grid(row=1, column=3, padx=10, pady=10)

        self.type_label = Label(self.data_frame, text="Type")
        self.type_label.grid(row=1, column=4, padx=10, pady=10)
        self.type_entry = OptionMenu(self.data_frame, self.menu2_value, *self.options2)
        self.type_entry.grid(row=1, column=5, padx=10, pady=10)

        self.invoice_label = Label(self.data_frame, text="Invoice")
        self.invoice_label.grid(row=1, column=6, padx=10, pady=10)
        self.invoice_entry = OptionMenu(self.data_frame, self.invoice_value, *self.options3)
        self.invoice_entry.grid(row=1, column=7, padx=10, pady=10)

        self.corp_label = Label(self.data_frame, text="Corporation")
        self.corp_label.grid(row=1, column=8, padx=10, pady=10)
        self.corp_menu = OptionMenu(self.data_frame, self.corp_value, *self.corporations)
        self.corp_menu.grid(row=1, column=9, padx=10, pady=10)

        self.Query.member_tree.bind("<<TreeviewSelect>>", self.select_record)

    def search(self):
        entry = str(self.search_entry.get().strip())
        if self.search_value.get() == "Last Name":
            self.Query.search_members(0,entry)
        elif self.search_value.get() == "First Name":
            self.Query.search_members(1,entry)
        elif self.search_value.get() == "Card Number":
            self.Query.search_members(2,entry)
        elif self.search_value.get() == "User Number":
            self.Query.search_members(3,entry)
        elif self.search_value.get() == "Phone Number":
            self.Query.search_members(4,entry)
        elif self.search_value.get() == "Expired/Expiring Soon":
            self.Query.search_expired()

    def update(self):
        entries = (self.ln_entry.get(), self.fn_entry.get(), self.cardnum_entry.get(), self.usernum_entry.get(), self.phonenum_entry.get(),
                   self.startday_entry.get(), self.end_entry.get(), self.menu2_value.get(), self.corp_value.get(), self.invoice_value.get())
        self.Query.update_record(entries)
        self.clear_entries()

    def delete(self):
        self.Query.delete()
        self.clear_entries()

    def add_to_family(self):
        entries = [self.ln_entry.get(), self.fn_entry.get(), self.cardnum_entry.get(), self.usernum_entry.get(), self.phonenum_entry.get(),
                   self.startday_entry.get(), self.end_entry.get(), self.menu2_value.get(), self.corp_value.get(), self.invoice_value.get()]

        def use_current_last_name():
            use_current_button.destroy()
            add_to_different_button.destroy()
            last_name_label.destroy()
            last_name_entry.destroy()
            entries[7] = 'Family'
            self.Query.update_record(tuple(entries))
            all_purpose_label.config(text=f'Successfully Added to {entries[0]} Family!')

        def add_to_different_family(family):
            use_current_button.destroy()
            add_to_different_button.destroy()
            last_name_label.destroy()
            last_name_entry.destroy()
            if len(family) < 1:
                all_purpose_label.config(text=f'Unsuccessful, no family name entered\nPlease close Tab')
            else:
                entries[1] = entries[1] + '-' + entries[0]
                entries[0] = family
                entries[7] = 'Family'
                self.Query.update_record(tuple(entries))
                all_purpose_label.config(text=f'Successfully Added to {family} Family!')

        if len(entries[5]) == 0 and len(entries[6]) == 0:
            self.Query.error_message()
            return

        family_popup = Toplevel()
        family_popup.geometry("500x300")
        family_popup.resizable(False,False)

        use_current_button = Button(family_popup, text="Use Current Last Name", command=use_current_last_name)
        use_current_button.pack()

        all_purpose_label = Label(family_popup, text=entries[0])
        all_purpose_label.pack()

        add_to_different_button = Button(family_popup, text="Add to Different Family", command=lambda: add_to_different_family(last_name_entry.get()))
        add_to_different_button.pack()

        last_name_label = Label(family_popup, text="Enter a Last Name:")
        last_name_label.pack()

        last_name_entry = Entry(family_popup)
        last_name_entry.pack()


    def select_record(self, e):
        self.clear_entries()
        values = self.Query.tree_value()
        if len(values)>1:
            self.fn_entry.insert(0, values[1])
            self.ln_entry.insert(0, values[0])
            self.cardnum_entry.insert(0, values[2])
            self.usernum_entry.insert(0, values[3])
            self.phonenum_entry.insert(0, values[4])
            self.startday_entry.insert(0, values[5])
            self.end_entry.insert(0, values[6])
            self.menu2_value.set(values[7])
            self.corp_value.set(values[9])
            self.invoice_value.set(values[8])

    def clear_entries(self):
        self.fn_entry.delete(0, END)
        self.ln_entry.delete(0, END)
        self.cardnum_entry.delete(0, END)
        self.usernum_entry.delete(0, END)
        self.phonenum_entry.delete(0, END)
        self.startday_entry.delete(0, END)
        self.end_entry.delete(0, END)
        self.menu2_value.set("Single")
        self.corp_value.set("N/A")
        self.invoice_value.set("No")

    def refresh_corps(self):
        self.corp_menu['menu'].delete(0, 'end')
        for corpo in self.Query.corporations:
            self.corp_menu['menu'].add_command(label=corpo, command=_setit(self.corp_value, corpo))

    def change_to_main(self):
        self.prevframe.pack(fill="both", expand=True)
        self.frame.pack_forget()