import time
import the_quizard as the_quizard

class player:

    def start_game(self):
        quotes = the_quizard.quizard_quotes

        print(quotes.get_quote(0))
        time.sleep(2)
        print(quotes.get_quote(1))
        time.sleep(2)
        print(quotes.get_quote(2))
        time.sleep(2)

        self.player_name = input(quotes.get_question(0))

        print(f"{quotes.get_quote(3)}".replace("%player_name%", self.player_name))
        time.sleep(4)
        print(quotes.get_quote(4))
        time.sleep(2)

        # choose question type and level
        self.question_type = int(input(f"{quotes.get_question(1)}".replace("%player_name%", self.player_name)))
        time.sleep(1)
        print(f"{quotes.get_quote(5)}".replace("%question_type%", self.__question_type_to_name__(self.question_type)))
        time.sleep(1)
        self.question_level = int(input(quotes.get_question(2)))
        time.sleep(1)
        print(f"{quotes.get_quote(6)}".replace("%question_level%", self.__question_level_to_name__(self.question_level)))
        time.sleep(3)
        print(quotes.get_quote(7))
        time.sleep(2)

    def __question_type_to_name__(self, question_type: int) -> str:
        if (question_type == 1):
            return "Addition"
        elif (question_type == 2):
            return "Subtraction"
        elif (question_type == 3):
            return "Multiplication"
        else:
            return "Division"

    def __question_level_to_name__(self, question_level: int) -> str:
        if (question_level == 1):
            return "Easy"
        elif (question_level == 2):
            return "Medium"
        else:
            return "Hard"

p = player()
p.start_game()
q = the_quizard.quizard(p.question_type, p.question_level)

question = q.get_question()
print(question.get_question_statement())
