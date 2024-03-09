import os
import time
from the_player import player as player
from the_quizard import quizard as quizard
from the_quizard import question as question
from the_quizard import quizard_quotes as quotes

def clear_screen():
    if (os.name == "NT"):
        os.system("cls")
    else:
        os.system("clear")

def get_type_and_level():
    player.question_type = int(input(f"{quotes.get_question(1)}".replace("%player_name%", player.player_name)))
    time.sleep(1)
    print(f"{quotes.get_quote(5)}".replace("%question_type%", player.question_type_to_name(player.question_type)))
    time.sleep(1)
    player.question_level = int(input(quotes.get_question(2)))
    time.sleep(1)
    print(f"{quotes.get_quote(6)}".replace("%question_level%", player.question_level_to_name(player.question_level)))
    time.sleep(2)

def ask_question():
    qz = quizard()
    q = qz.get_question(player.question_type, player.question_level)
    a = int(input(f"{quotes.get_quote(8)}".replace("%question_statement%", q.get_question_statement())))

    if (a == q.get_answer()):
        print(quotes.get_random_success())
    else:
        print(quotes.get_random_failure(q.get_answer()))


clear_screen()
print(quotes.get_quote(0))
time.sleep(1)
print(quotes.get_quote(1))
time.sleep(1)
print(quotes.get_quote(2))
time.sleep(1)

player.player_name = input(quotes.get_question(0))

print(f"{quotes.get_quote(3)}".replace("%player_name%", player.player_name))
time.sleep(1)
print(quotes.get_quote(4))
time.sleep(1)

clear_screen()
get_type_and_level()

print(quotes.get_quote(7))
time.sleep(2)

while True:
    clear_screen()
    ask_question()

    if (input("Would you like another question (y/n)?") == "n"):
        break