# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizBrain: 
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        u_input = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ")
        self.checkAnswer(question, u_input)

    def still_have_questions(self):
        return len(self.question_list) - self.question_number > 0

    def checkAnswer(self, question, u_input):
        if question.answer == u_input:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was {question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong")
            print(f"The correct answer was {question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")

