import tkinter as tk
from tkinter import messagebox

# List of questions, options, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "PHP", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x350")
        
        self.q_no = 0
        self.selected_answers = [tk.StringVar() for _ in questions]
        
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", font=("Arial", 12), variable=self.selected_answers[self.q_no], value="", anchor="w", justify="left")
            btn.pack(fill='x', padx=50, pady=2)
            self.radio_buttons.append(btn)

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(pady=20)

        self.prev_button = tk.Button(self.nav_frame, text="Previous", command=self.prev_question)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=1, padx=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.show_score)
        self.submit_button.pack(pady=10)

    def display_question(self):
        q_data = questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}: {q_data['question']}")

        for i, option in enumerate(q_data["options"]):
            self.radio_buttons[i].config(text=option, value=option, variable=self.selected_answers[self.q_no])
            self.radio_buttons[i].deselect()

        # Set previous selected value
        selected_value = self.selected_answers[self.q_no].get()
        if selected_value:
            self.selected_answers[self.q_no].set(selected_value)

        # Disable previous button at start
        self.prev_button.config(state=tk.NORMAL if self.q_no > 0 else tk.DISABLED)

        # Change next to disabled at last question
        self.next_button.config(state=tk.NORMAL if self.q_no < len(questions) - 1 else tk.DISABLED)

    def next_question(self):
        if self.q_no < len(questions) - 1:
            self.q_no += 1
            self.display_question()

    def prev_question(self):
        if self.q_no > 0:
            self.q_no -= 1
            self.display_question()

    def show_score(self):
        score = 0
        for idx, q in enumerate(questions):
            if self.selected_answers[idx].get() == q["answer"]:
                score += 1
        messagebox.showinfo("Result", f"Your Score: {score}/{len(questions)}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
 