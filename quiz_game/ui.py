from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(
            text="Score:0", 
            font=("Arial", 14, "bold"), 
            fg="white", 
            bg=THEME_COLOR, 
            highlightthickness=0
        )
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="text", 
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="quiz_game/images/true.png")
        self.true_button = Button(image=true_image, pady=50, highlightthickness=0, command=self.answer_is_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="quiz_game/images/false.png")
        self.false_button = Button(image=false_image, pady=50, highlightthickness=0, command=self.answer_is_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_have_questions():
            self.score_text.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thats all folks!")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def answer_is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_is_false(self):
         self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

