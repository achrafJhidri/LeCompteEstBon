import tkinter as tk

class CountDownMsgBox(tk.Toplevel):
    TEXT_FONT = ('Helevtica', 12, 'bold')
    TEXT = "This process may take up to 2 min. Please try after 2min..!"
    TIMER_FONT = ('Helevtica', 16, 'bold')
    TIMER_COUNT= 10 # Seconds
    WIDTH  = 300
    HEIGHT = 300
    def __init__(self, master, vue, msg_text=TEXT, sec=0):
        CountDownMsgBox.TIMER_COUNT  = sec
        tk.Toplevel.__init__(self, master=master)
        self.vue=vue
        self.master = master
        self.msg_text = msg_text
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 100, y + 200))
        self.build()

    def build(self):
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, padx=20, pady=20)

        message_var = tk.StringVar(self.master, self.msg_text)
        tk.Label(main_frame, padx=10, font=self.TEXT_FONT,
                 compound='left', textvariable=message_var, wraplength=200,
                 fg='gray40').grid(row=0, column=0)

        self.timer_var = tk.StringVar()
        tk.Label(main_frame, textvariable=self.timer_var, font=self.TIMER_FONT,
                 fg='blue').grid(row=1, column=0, padx=20, pady=20)

        self.count_down()

    def count_down(self, time_count=TIMER_COUNT):
        self.timer_var.set("{} Secondes".format(time_count))
        if time_count == 0:
            self.destroy()
            self.vue.on_back()
            #self.app.count_down_callback()
        time_count -= 1
        self.after(1000, self.count_down, time_count)