from question_model import Question
from data import get_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for questions in get_data():
    new_q = Question(questions['question'], questions['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

quiz.next_question()
