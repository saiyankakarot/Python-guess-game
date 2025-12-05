import ttkbootstrap as tb
from ttkbootstrap.constants import *
import random
import time
import os
import winsound  # <-- for system beeps

LEADERBOARD_FILE = "leaderboard.txt"

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Number Guessing Game")
        self.root.geometry("500x450")
        self.style = tb.Style(theme='darkly')
        
        self.main_frame = tb.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.difficulty_levels = {"Easy":50, "Medium":100, "Hard":500}
        self.theme = 'darkly'

        self.start_screen()

    # ---------- Start Screen ----------
    def start_screen(self):
        self.clear_frame()
        tb.Label(self.main_frame, text="Number Guessing Game", font=("Arial", 18, "bold")).pack(pady=10)

        tb.Label(self.main_frame, text="Select Difficulty", font=("Arial", 14)).pack(pady=10)
        for diff in self.difficulty_levels:
            tb.Button(self.main_frame, text=diff, bootstyle=SUCCESS, width=20, 
                      command=lambda d=diff: self.start_game(d)).pack(pady=5)
        
        tb.Button(self.main_frame, text="Switch Theme", bootstyle=INFO, width=20,
                  command=self.switch_theme).pack(pady=10)
        tb.Button(self.main_frame, text="View Leaderboard", bootstyle=PRIMARY, width=20,
                  command=self.show_leaderboard).pack(pady=5)

    # ---------- Theme Switch ----------
    def switch_theme(self):
        self.theme = 'flatly' if self.theme=='darkly' else 'darkly'
        self.style = tb.Style(theme=self.theme)

    # ---------- Initialize Game ----------
    def start_game(self, difficulty):
        self.clear_frame()
        self.lowest_num = 1
        self.highest_num = self.difficulty_levels[difficulty]
        self.answer = random.randint(self.lowest_num, self.highest_num)
        self.guesses = 0
        self.max_attempts = 7
        self.prev_guess = None
        self.start_time = time.time()
        self.current_difficulty = difficulty

        tb.Label(self.main_frame, text=f"Difficulty: {difficulty}", font=("Arial",14)).pack(pady=5)
        tb.Label(self.main_frame, text=f"Guess a number between {self.lowest_num} and {self.highest_num}", font=("Arial",12)).pack(pady=5)

        self.guess_entry = tb.Entry(self.main_frame, font=("Arial",14))
        self.guess_entry.pack(pady=10)
        
        self.submit_btn = tb.Button(self.main_frame, text="Submit Guess", bootstyle=SUCCESS, command=self.check_guess)
        self.submit_btn.pack(pady=5)

        self.feedback_label = tb.Label(self.main_frame, text="", font=("Arial",12))
        self.feedback_label.pack(pady=10)

        self.progress = tb.Progressbar(self.main_frame, length=300, maximum=self.max_attempts, bootstyle=INFO)
        self.progress.pack(pady=10)

        self.timer_label = tb.Label(self.main_frame, text="Time: 0s", font=("Arial",12))
        self.timer_label.pack(pady=5)
        self.update_timer()

    # ---------- Update Timer ----------
    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed}s")
        self.timer_id = self.root.after(1000, self.update_timer)

    # ---------- Check Guess ----------
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guess_entry.delete(0, tk.END)
        except ValueError:
            self.feedback_label.config(text="Enter a valid number!", foreground="orange")
            winsound.Beep(400,200)  # beep for invalid input
            return

        if guess < self.lowest_num or guess > self.highest_num:
            self.feedback_label.config(text="Out of bounds!", foreground="orange")
            winsound.Beep(400,200)  # beep for out of bounds
            return

        self.guesses +=1
        self.progress['value'] = self.guesses

        # Warmer/Colder hints
        if self.prev_guess is not None:
            if abs(guess - self.answer) < abs(self.prev_guess - self.answer):
                self.feedback_label.config(text="Warmer 🔥", foreground="purple")
            else:
                self.feedback_label.config(text="Colder ❄️", foreground="blue")
        self.prev_guess = guess

        # Check guess
        if guess < self.answer:
            self.feedback_label.config(text="Too low!", foreground="red")
            winsound.Beep(500,150)  # beep for wrong guess
        elif guess > self.answer:
            self.feedback_label.config(text="Too high!", foreground="red")
            winsound.Beep(500,150)  # beep for wrong guess
        else:
            winsound.Beep(1000,300)  # beep for correct guess
            self.win_game()
            return

        # Max attempts reached
        if self.guesses >= self.max_attempts:
            winsound.Beep(300,300)  # beep for game over
            tb.messagebox.showinfo("Game Over", f"You ran out of attempts!\nAnswer: {self.answer}")
            self.start_screen()

    # ---------- Win ----------
    def win_game(self):
        elapsed_time = int(time.time() - self.start_time)
        tb.messagebox.showinfo("Correct!", f"You guessed it!\nAnswer: {self.answer}\nAttempts: {self.guesses}\nTime: {elapsed_time}s")
        self.save_score(self.current_difficulty, self.guesses, elapsed_time)
        self.root.after_cancel(self.timer_id)
        self.start_screen()

    # ---------- Save Score ----------
    def save_score(self, difficulty, guesses, time_taken):
        leaderboard = self.load_leaderboard()
        if difficulty not in leaderboard or \
           guesses < leaderboard[difficulty]['guesses'] or \
           (guesses==leaderboard[difficulty]['guesses'] and time_taken<leaderboard[difficulty]['time']):
            leaderboard[difficulty] = {'guesses':guesses, 'time':time_taken}
        with open(LEADERBOARD_FILE,'w') as f:
            for diff, data in leaderboard.items():
                f.write(f"{diff},{data['guesses']},{data['time']}\n")

    # ---------- Load Leaderboard ----------
    def load_leaderboard(self):
        leaderboard = {}
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE,'r') as f:
                for line in f:
                    diff, g, t = line.strip().split(',')
                    leaderboard[diff] = {'guesses':int(g),'time':int(t)}
        return leaderboard

    # ---------- Show Leaderboard ----------
    def show_leaderboard(self):
        leaderboard = self.load_leaderboard()
        if not leaderboard:
            tb.messagebox.showinfo("Leaderboard", "No scores yet!")
            return
        text = ""
        for diff, data in leaderboard.items():
            text += f"{diff}: {data['guesses']} guesses, {data['time']}s\n"
        tb.messagebox.showinfo("Leaderboard", text)

    # ---------- Utility ----------
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# ---------- Run ----------
import tkinter as tk
root = tk.Tk()
app = NumberGuessingGame(root)
root.mainloop()
