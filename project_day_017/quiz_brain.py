class QuizBrain:
    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

# TODO: asking the questions

# TODO: checking if the answer was correct

# TODO: checking if we're at the end of the quiz

