import the_quizard as the_quizard

class player:

    def start_game(self):

        print("Welcome to the Quizard Game!!!")
        print("I'm your host... The Quizard!!!")
        print("Let's meet our contestant!!!")

        self.player_name = input("Tell us your name player: ")

        print(f"Welcome to the game {self.player_name}!!!")
        print("Let's get started!!!")

        self.question_level = input(f"{self.player_name}, first pick your question dificulty (1/2/3): ")
        self.question_type = input(f"{self.player_name}, now pick your question type (1/2/3/4): ")
        
        print(f"The player chose {self.__question_level_to_name__(self.question_level)}")

        print("That's great, here's your first question...")
        # question_level = input("")

    def __question_level_to_name__(self, question_level: int) -> str:
        if (question_level == 1):
            return "Addition"
        elif (question_level == 2):
            return "Subtraction"
        elif (question_level == 3):
            return "Multiplication"
        else:
            return "Division"



p = player()
p.start_game()