class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(choice, current_question.answer)

    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"The answer was {correct_ans}.")
        print(f"Current Score: {self.score}/{self.question_number}")
        print("\n")
