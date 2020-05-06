import queue
from tkinter import messagebox

from view.Pseudo import Pseudo
import tkinter as tk


class View(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.frame = Pseudo(controller, self)

        #screen_height = int(self.winfo_screenheight() * 1/2)
        #screen_width = self.winfo_screenwidth()

        #screen_width = int(screen_width *3/8)

        #self.geometry("{0}x{1}".format(screen_width, screen_height))

        self.title("Le compte est bon")

        self.geometry("650x600")

        self.controller = controller

        self.queue=queue.Queue()
        self.running=1
        self.periodicCall()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            print(self.frame)
            self.destroy()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        while self.queue.qsize() > 0:
            self.queue.get().run()


        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.after(100, self.periodicCall)


    def goMenuPrincipale(self):
        self.frame.forget()
        self.frame=Pseudo(controller=self.controller,master=self)

    def endApplication(self):
        self.running = 0
