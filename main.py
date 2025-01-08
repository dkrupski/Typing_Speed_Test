from tkinter import *
import time
from tkinter import messagebox

FONT_NAME = "Courier"
GREEN = "#9bdeac"
BLUE = "#C6CECE"

class TypingSpeedTest:

    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.start_time = None

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. "
            "This is a sample text to test your typing speed. "
            "Type it as fast as you can and see your performance!"
        )

        self.instructions_label = Label(text="Type the text below as fast as you can:", font=(FONT_NAME, 12), bg=GREEN)
        self.instructions_label.grid(column=0, row=0)

        self.sample_label = Label(text=self.sample_text, wraplength=400, font=(FONT_NAME, 12), justify="center",
                                  bg=BLUE)
        self.sample_label.grid(column=0, row=1)

        self.text_area = Text(height=10, width=50, wrap=WORD, font=(FONT_NAME, 12))
        self.text_area.grid(column=1, row=1)
        self.text_area.bind("<FocusIn>", self.start_timer)

        self.submit_button = Button(text="Submit", command=self.calculate_speed, font=(FONT_NAME, 12))
        self.submit_button.grid(column=1, row=2)

    def start_timer(self, event=None):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showwarning("Warning", "You haven't started typing yet!")
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time
        entered_text = self.text_area.get("1.0", END).strip()

        word_count = len(entered_text.split())
        time_in_minutes = elapsed_time / 60
        words_per_minute = round(word_count / time_in_minutes, 2)

        sample_words = self.sample_text.split()
        entered_words = entered_text.split()
        correct_words = sum(1 for sw, ew in zip(sample_words, entered_words) if sw == ew)

        accuracy = round((correct_words / len(sample_words)) * 100, 2)

        messagebox.showinfo(
            "Typing Speed Results",
            f"Time taken: {elapsed_time:.2f} seconds\n"
            f"Words typed: {word_count}\n"
            f"Words per minute (WPM): {words_per_minute}\n"
            f"Accuracy: {accuracy}%"
        )

        self.reset_test()

    def reset_test(self):
        self.text_area.delete("1.0", END)
        self.start_time = None




if __name__ == "__main__":
    root = Tk()
    app = TypingSpeedTest(root)
    root.mainloop()