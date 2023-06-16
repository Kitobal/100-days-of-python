from question_model import Question
from data import film_questions
from quiz_brain import QuizBrain

question_bank = []
for q in film_questions:
    text = q["question"]
    answer = q["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final Score was: {quiz.score}/{len(question_bank)}")