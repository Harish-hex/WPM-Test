from tkinter import *
from timeit import default_timer as timer
import random

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("600x400")

        # Load sentences from the file
        try:
            with open("sentences.txt", "r") as file:
                self.sentences = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("Sentences file not found. Using default sentences.")

            # Default sentences if the file is not found
            self.sentences = [
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

        
        self.text = random.choice(self.sentences)
        self.start_time = None

        self.title_label = Label(master, text="Typing Speed Test", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=5)

        self.instruction_label = Label(master, text="Type the sentence below as fast and accurately as you can.")
        self.instruction_label.pack(pady=5)

        self.text_display = Text(master, height=3, width=60, wrap='word', font=("Courier", 12))
        self.text_display.insert(END, self.text)
        self.text_display.config(state=DISABLED, bg="white", fg="black")
        self.text_display.pack(pady=10)

        self.entry = Entry(master, width=60, font=("Courier", 12), fg="black", bg="lightyellow")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_text)

        self.result_label = Label(master, text="")
        self.result_label.pack(pady=10)

        self.reset_button = Button(master, text="Try Again", command=self.reset_test)
        self.reset_button.pack(pady=5)

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

    def reset_test(self):
        self.text = random.choice(self.sentences)
        self.text_display.config(state=NORMAL)
        self.text_display.delete("1.0", END)
        self.text_display.insert(END, self.text)
        self.text_display.config(state=DISABLED)
        self.entry.config(state=NORMAL)
        self.entry.delete(0, END)
        self.result_label.config(text="")
        self.start_time = None

if __name__ == "__main__":
    root = Tk()
    app = TypingTest(root)
    root.mainloop()
