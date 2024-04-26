import tkinter as tk
from time import time
from random import choice

class TypeSpeed:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed")
        self.root.geometry("850x400")  # Adjusted window height
        self.texts = open("/Users/manjilrawal/Downloads/Personal_Project/texts.txt", 'r').read().split("\n")

        self.frame = tk.Frame(self.root)
        self.sample_label = tk.Label(self.frame, font=("Helvetica", 18), text="")
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=2, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress-Return>", self.start_typing)  # Bind Enter key
        self.input_entry.bind("<Key>", self.update_text)  # Bind all other keys

        self.timer_label = tk.Label(self.frame, font=("Helvetica", 18), text="Time left: 30 sec")
        self.timer_label.grid(row=2, column=0, columnspan=2, padx=2, pady=5)

        self.speed_label = tk.Label(self.frame, font=("Helvetica", 18),
                                    text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        self.speed_label.grid(row=3, column=0, columnspan=2, padx=2, pady=5)

        self.reset_btn = tk.Button(self.frame, fg="green", bg="yellow", text="Reset", font=("Helvetica", 18),
                                   command=self.reset)
        self.reset_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)
        self.start_time = None
        self.running = False
        self.remaining_time = 30
        self.root.mainloop()

    def start_typing(self, event):
        if not self.running and event.keysym != "Return":  # Exclude Enter key
            self.running = True
            self.start_time = time()
            self.remaining_time = 30
            self.update_timer()

        if self.input_entry.get() == self.sample_label.cget("text"):
            self.running = False
            self.calculate_speed()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time} sec")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.running = False
            self.calculate_speed()

    def update_text(self, event):
        if not self.running:
            new_text = self.input_entry.get()
            self.sample_label.config(text=new_text)

    def calculate_speed(self):
        elapsed_time = 30 - self.remaining_time
        total_chars = len(self.input_entry.get())
        cps = total_chars / elapsed_time
        cpm = cps * 60
        total_words = len(self.input_entry.get().split())
        wps = total_words / elapsed_time
        wpm = wps * 60  # Calculate WPM based on entire 30-second interval
        self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")

    # Reset the application when the reset button is pressed
    def reset(self):
        self.running = False
        self.input_entry.delete(0, tk.END)
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        new_text = choice(self.texts)
        self.sample_label.config(text=new_text)  # Update text dynamically
        self.timer_label.config(text="Time left: 30 sec")
        self.remaining_time = 30
        self.start_time = None

TypeSpeed()
