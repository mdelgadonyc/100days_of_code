from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)

        # Window question window (300x250) with text in Arial, 20, italic
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_button_img, highlightthickness=0, borderwidth=0,
                                  command=self.check_answer_for_true)
        self.false_button = Button(image=false_button_img, highlightthickness=0, borderwidth=0,
                                   command=self.check_answer_for_false)
# btn = tk.Button(root, text="Press", command=lambda: func("See this worked!"))
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def check_answer_for_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_answer_for_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)

