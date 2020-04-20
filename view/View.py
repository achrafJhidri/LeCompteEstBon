import queue
from view.Pseudo import Pseudo
import tkinter as tk


class View(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.frame = Pseudo(controller, self)

        screen_height = int(self.winfo_screenheight() * 1/2)
        screen_width = self.winfo_screenwidth()

        screen_width = int(screen_width *3/8)

        self.geometry("{0}x{1}".format(screen_width, screen_height))

        self.controller = controller

        self.queue=queue.Queue()
        self.running=1
        self.periodicCall()


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
        print("on est tous la")
        self.frame.forget()
        self.frame=Pseudo(controller=self.controller,master=self)

    def endApplication(self):
        self.running = 0
