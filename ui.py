from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score text
        self.score_label = Label(text=f"Score 0", font=('Arial', 14, 'normal'), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas_quiz = Canvas(width=300, height=250)
        self.question_text = self.canvas_quiz.create_text(150, 125, width=280, text="Amazon acquired twitch in August 2014 for $970 million dollars.",
                                     font=('Arial', 20, 'italic'))
        self.canvas_quiz.grid(column=0, row=1, columnspan=2, pady=50)

        right_file = PhotoImage(file="images/true.png")
        self.button_right = Button(image=right_file, command=self.right_pressed)
        self.button_right.grid(column=0, row=2)

        wrong_file = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=wrong_file, command=self.wrong_pressed)
        self.button_wrong.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas_quiz.config(bg="white")
            self.score_label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas_quiz.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas_quiz.itemconfig(self.question_text, text="You have reached end of the question's")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_quiz.config(bg="green")

        else:
            self.canvas_quiz.config(bg="red")
        self.window.after(1000, self.get_next_question())

