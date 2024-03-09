import random

class question:
    def __init__(self, num1: int, num2: int, question_type: int):
        self.num1 = num1
        self.num2 = num2
        self.question_type = question_type

    def get_question_statement(self) -> str:
        return f"{self.num1} {self.__question_type_to_symbol__(self.question_type)} {self.num2}"
    
    def __question_type_to_symbol__(self, question_type: int) -> str:
        if (question_type == 1):
            return "+"
        elif (question_type == 2):
            return "-"
        elif (question_type == 3):
            return "*"
        else:
            return "/"
    
    def get_answer(self) -> int:
        if (self.question_type == 1):
            return self.num1 + self.num2
        elif (self.question_type == 2):
            return self.num1 - self.num2
        elif (self.question_type == 3):
            return self.num1 * self.num2
        else:
            return self.num1 / self.num2

class quizard_quotes:
    quotes = [
        "Welcome to the Quizard Game!!!",
        "I'm your host... The Quizard!!!",
        "Let's meet our contestant!!!",
        "Welcome to the game %player_name%!!!",
        "Let's get started!!!",
        "Great you chose %question_type%!",
        "Great you chose %question_level%!",
        "Let's get started with your first question.",
        "What is the answer to: %question_statement%? "
    ]

    questions = [
        "Tell us your name player: ",
        "%player_name%, first pick your question type (1/2/3/4): ",
        "And now pick your question level (1/2/3): "
    ]

    successes = [
        "You're right!!! Nice job!!",
        "Wow, you got it right!!",
        "Right on, great answer!!",
        "You got it right!!"
    ]

    failures = [
        "Oh, sorry, that's not right. The correct answer was %correct_answer%",
        "That's no the right answer. The answer was %correct_answer%",
        "No, the answer was %correct_answer%, try again.",
        "Too bad, that's not right. The right answer was %correct_answer%"
    ]

    def get_quote(idx: int) -> str:
        return quizard_quotes.quotes[idx]
    
    def get_question(idx: int) -> str:
        return quizard_quotes.questions[idx]
    
    def get_random_success() -> str:
        return quizard_quotes.successes[random.randint(0, len(quizard_quotes.successes) -1)]

    def get_random_failure(correct_answer: int) -> str:
        return f"{quizard_quotes.failures[random.randint(0, len(quizard_quotes.failures) -1)]}".replace("%correct_answer%", str(correct_answer))

class quizard:
    
    def get_question(self, question_type: int, question_level: int) -> question:
        num1 = self.get_random_number(question_level)
        num2 = self.get_random_number(question_level)

        if (num1 > num2):
            q = question(num1, num2, question_type)
        else:
            q = question(num2, num1, question_type)

        return q

    def get_random_number(self, question_level: int) -> int:
        if (question_level == 1):
            return random.randint(1, 9)
        elif (question_level == 2):
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)
