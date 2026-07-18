from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

def fill_question_bank(question_data, question_bank):
    for question in question_data:
        t= question["text"]
        a = question["answer"]
        quest = Question(t, a)
        question_bank.append(quest)

def main():
    fill_question_bank(question_data, question_bank)
    quizbrain = QuizBrain(question_bank)
    while quizbrain.still_have_questions():
        quizbrain.next_question()

if __name__ == "__main__":
    main()