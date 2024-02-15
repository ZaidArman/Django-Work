import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.questions = [
            (
                "What is the capital of France?",
                ["Berlin", "Madrid", "Paris", "Rome"],
                "Paris"
            ),
            (
                "Which planet is known as the Red Planet?",
                ["Venus", "Mars", "Jupiter", "Saturn"],
                "Mars"
            ),
            (
                "What is the largest mammal in the world?",
                ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "Blue Whale"
            ),
            (
                "Who wrote 'Romeo and Juliet'?",
                ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
                "William Shakespeare"
            ),
            (
                "What is the capital of Japan?",
                ["Beijing", "Tokyo", "Seoul", "Bangkok"],
                "Tokyo"
            ),
            # Add more questions as needed
        ]

        self.current_question_index = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_question = tk.Label(self.master, text="")
        self.label_question.pack(pady=10)

        self.var_selected_option = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.master, text="", variable=self.var_selected_option, value=i)
            radio_button.pack()

            self.radio_buttons.append(radio_button)

        self.button_skip = tk.Button(self.master, text="Skip", command=self.skip_question)
        self.button_skip.pack(pady=10)

        self.button_submit = tk.Button(self.master, text="Submit", command=self.submit_quiz)
        self.button_submit.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data[0])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data[1][i])

            self.var_selected_option.set(-1)  # Deselect all radio buttons

        else:
            self.show_results()

    def skip_question(self):
        self.current_question_index += 1
        self.load_question()

    def submit_quiz(self):
        selected_option = self.var_selected_option.get()

        if selected_option == -1:
            messagebox.showinfo("Quiz App", "Please select an answer.")
        else:
            question_data = self.questions[self.current_question_index]
            correct_answer_index = question_data[1].index(question_data[2])

            if selected_option == correct_answer_index:
                self.score += 1

            self.current_question_index += 1
            self.load_question()

    def show_results(self):
        messagebox.showinfo("Quiz App", f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
