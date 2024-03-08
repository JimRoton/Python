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
    
    # def question_answer(self, num1: int, num2: int, question_type: int) -> int:
    #     if (question_type == 1):
    #         return num1 + num2
    #     elif (question_type == 2):
    #         return num1 - num2
    #     elif (question_type == 3):
    #         return num1 * num2
    #     else:
    #         return num1 / num2

class quizard_quotes:
    quotes = [
        "Welcome to the Quizard Game!!!",
        "I'm your host... The Quizard!!!",
        "Let's meet our contestant!!!",
        "Welcome to the game %player_name%!!!",
        "Let's get started!!!",
        "Great you chose %question_type%!",
        "Great you chose %question_level%!",
        "Let's get started with your first question."
    ]

    questions = [
        "Tell us your name player:",
        "%player_name%, first pick your question type (1/2/3/4):",
        "And now pick your question level (1/2/3):"
    ]

    successes = []

    failures = []

    def get_quote(idx: int) -> str:
        return quizard_quotes.quotes[idx]
    
    def get_question(idx: int) -> str:
        return quizard_quotes.questions[idx]
    
    def get_random_success() -> str:
        pass

    def get_random_failure() -> str:
        pass

class quizard:

    def __init__(self, question_type: int, question_level: int) -> question:
        self.question_type = question_type
        self.question_level = question_level
    
    def get_question(self):
        
        #addition
        if (self.question_type == 1):
            q = question(1, 5, 1)
            return q

        #subtraction
        elif (self.question_type == 2):
            print("subtraction")

        #multiplication
        elif (self.question_type == 3):
            print("multiplication")

        #division
        else:
            print("division")
