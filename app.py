from collections import deque
import tkinter as tk
from tkinter import ttk
from frames import Timer,Settings

class PomodoroTimer(tk.Tk):
    """This creates the basic skeleton of the Timer app.
       It has main window and container within it.
       This owns the controlling the time and the app configuration
    """
    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        
        # Root Frame
        self.title("Pomodoro Timer")
        self.columnconfigure(0,weight =1)
        self.rowconfigure(0, weight = 1)
        
        # The next three values are for setting apps to change the timer configuration
        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        
        # Container Frame
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0,weight=1)
        
        # timer_frame = Timer(container, self)
        # timer_frame.grid(row=0,column=0, sticky="NESW")
        settings_frame = Settings(container, self)
        settings_frame.grid(row=0,column=0, sticky="NESW")
        

app = PomodoroTimer()
app.mainloop()