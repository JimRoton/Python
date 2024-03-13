import random
from datetime import datetime as datetime

class colors:
    default = "\033[0m"
    green   = "\033[32m"
    red     = "\033[31m"
    yellow  = "\033[33m"
    blue    = "\033[34m"
    purple  = "\033[35"
    cyan    = "\033[36"

    random_colors  = [
        "\033[31m",
        "\033[32m",
        "\033[33m",
        "\033[34m",
        "\033[35m",
        "\033[36m"
    ]

    def get_random_color():
        i = len(colors.random_colors) -1
        return colors.random_colors[random.randint(0, i)]

class question:
    answer: int
    start_time: datetime
    end_time: datetime

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

    def get_total_time(self) -> int:
        return (self.end_time - self.start_time).seconds

class quotes:
    quotes = [
        "Welcome to the Quizard Game!!!",
        "I'm your host... The Quizard!!!",
        "Let's meet our contestant!!!",
        "Welcome to the game %color%%player_name%%default_color%!!!",
        "Let's get started!!!",
        "Great you chose %color%%question_type%%default_color%!",
        "Great you chose %color%%question_level%%default_color%!",
        "Let's get started with your first question.",
        "What is the answer to: %color%%question_statement%%default_color%? ",
        "You won %color%%win%%default_color% times and lost %color%%loss%%default_color% times.",
        "Addition         = 1\nSubtraction      = 2\nMultiplication   = 3\nDivision         = 4",
        "Easy             = 1\nMedium           = 2\nHeard            = 3\n",
        "You took %color%%seconds%%default_color% seconds on this question.",
        "Your game took a total of %color%%total_time%%default_color% seconds."
    ]

    questions = [
        "Tell us your name player: ",
        "%color%%player_name%%default_color%, first pick your question type...",
        "And now pick your question level...",
        "Would you like to play again (Y/N)?"
    ]

    successes = [
        "You're right! Nice job!",
        "Wow, you got it right!",
        "Right on, great answer!",
        "You got it right!"
    ]

    failures = [
        "Oh, sorry, that's not right. The correct answer was %color%%correct_answer%%default_color%",
        "That's not the right answer. The answer was %color%%correct_answer%%default_color%",
        "No, the answer was %color%%correct_answer%%default_color%, try again.",
        "Too bad, that's not right. The right answer was %color%%correct_answer%%default_color%"
    ]

    def get_quote(idx: int, color: str = colors.green) -> str:
        return f"{quotes.quotes[idx]}".replace("%color%", color).replace("%default_color%", colors.default)
    
    def get_question(idx: int, color: str = colors.green) -> str:
        return f"{quotes.questions[idx]}".replace("%color%", color).replace("%default_color%", colors.default)

    def get_random_success() -> str:
        return f"{quotes.successes[random.randint(0, len(quotes.successes) -1)]}"

    def get_random_failure(correct_answer: int, color: str) -> str:
        return f"{quotes.failures[random.randint(0, len(quotes.failures) -1)]}".replace("%correct_answer%", str(correct_answer)).replace("%color%", color).replace("%default_color%", colors.default)

    def get_rainbow_quote(idx: int) -> str:
        str = quotes.quotes[idx]
        rtn = ""

        for chr in str:
            rtn += colors.get_random_color() + chr
        
        return rtn + colors.default

class quizard:
    player_name: str = "Player Name"
    question_type: int = 0
    question_level: int = 0

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

    def question_type_to_name(question_type: int) -> str:
        if (question_type == 1):
            return "Addition"
        elif (question_type == 2):
            return "Subtraction"
        elif (question_type == 3):
            return "Multiplication"
        else:
            return "Division"

    def question_level_to_name(question_level: int) -> str:
        if (question_level == 1):
            return "Easy"
        elif (question_level == 2):
            return "Medium"
        else:
            return "Hard"
