#b00152481
#24/03/25
#part1

from tkinter import*
class myFirstGUI:
    def__init__(self, master):
        self.master=master
        master.title("A simple GUI")

        self.label1=Label(master,
    text="Firstname:")
        self.label1.pack()
        self.entry1=Entry()
        self.entry1.pack()

        self.label2 = Label(master,
    text = "Surname:")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry.pack()

        self.label3 = Label(master,text ="Date of Birth:")
        self.label3.pack()
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master,
    text = "Member Type:")
        self.label4.pack()
        self.entry4 = Entry()
        self.entry4.pack()

        self.insert_buttton = Button(master,
    text="Print All Members",
        command = self.print_all_members)
        self.close_button.pack()

        self.close_button = Button(master,
    text = "Close", command = self.close)
        self.close_button.pack()

        def insert_into_db(self):
            print("Firstname:", self.entry1.get())
            print("Surname:", self.entry2.get())
            print("Date of Birth", self.entry3.get())
            print("Member Type:", self.entry4.get())

        def print_all_members(self):
            print("Printing all members:")
            print("Firstname:", self.entry1.get())
            print("Surname:", self.entry2.get())

        def close(self):
            self.master.destroy()

        root = Tk()
        my_gui = myFirstGUI(root)
        root.mainloop()
        
        
