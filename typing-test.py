from tkinter import *
from timeit import default_timer as timer
import random

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")

        sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing is a useful skill in the digital world.",
        "Python is a powerful and easy-to-learn language.",
        "Practice makes perfect in every field.",
        "Time waits for no one, so make it count.",
        "Always think before you code.",
        "Hard work beats talent when talent doesn't work hard.",
        "A journey of a thousand miles begins with a single step.",
        "Errors are part of the learning process.",
        "Stay curious, keep learning, and never give up."
     ]
        
        self.text = random.choice(sentences)
        self.start_time = None
        
        self.label = Label(master, text=self.text)
        self.label.pack(pady=10)
        
        self.entry = Entry(master, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_text)
        
        self.result_label = Label(master, text="")
        self.result_label.pack(pady=10)

    def check_text(self, event):
        if not self.start_time:
            self.start_time = timer()
        
        typed_text = self.entry.get()
        if typed_text == self.text:
            elapsed_time = timer() - self.start_time
            wpm = (len(typed_text.split()) / elapsed_time) * 60
            self.result_label.config(text=f"Well done! Your speed: {wpm:.2f} WPM")
            self.entry.config(state='disabled')
        else:
            self.result_label.config(text="Keep typing...")

if __name__ == "__main__":
    root = Tk()
    app = TypingTest(root)
    root.mainloop()