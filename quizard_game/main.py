import os
import time
from the_quizard import colors as colors, quizard as quizard, question as question, quotes as quotes

def clear_screen():
    if (os.name == "NT"):
        os.system("cls")
    else:
        os.system("clear")

def get_type_and_level():
    print(f"{quotes.get_question(1)}".replace("%player_name%", quizard.player_name))
    print(quotes.get_quote(10))
    quizard.question_type = int(input("Question Type: "))
    time.sleep(1)
    print(f"{quotes.get_quote(5)}".replace("%question_type%", quizard.question_type_to_name(quizard.question_type)))
    time.sleep(2)

    print(quotes.get_question(2))
    print(quotes.get_quote(11))
    quizard.question_level = int(input("Question Level: "))
    time.sleep(1)
    print(f"{quotes.get_quote(6)}".replace("%question_level%", quizard.question_level_to_name(quizard.question_level)))
    time.sleep(2)

def ask_question() -> bool:
    qz = quizard()
    q = qz.get_question(quizard.question_type, quizard.question_level)

    a = int(input(f"{quotes.get_quote(8)}".replace("%question_statement%", q.get_question_statement())))

    if (a == q.get_answer()):
        print(quotes.get_random_success())
        return True
    else:
        print(quotes.get_random_failure(q.get_answer(), colors.green))
        return False

def start_game() -> any:
    i = 1
    win = 0
    loss = 0
    while (i <= 10):
        clear_screen()

        print (f"Question {i}:")
        if (ask_question()):
            win += 1
        else:
            loss += 1
    
        i += 1
        time.sleep(3)

    return win, loss

def main():
    clear_screen()
    print(quotes.get_rainbow_quote(0))
    time.sleep(1)
    print(quotes.get_quote(1))
    time.sleep(1)
    print(quotes.get_quote(2))
    time.sleep(1)

    quizard.player_name = input(quotes.get_question(0))

    print(f"{quotes.get_quote(3)}".replace("%player_name%", quizard.player_name))
    time.sleep(1)
    print(quotes.get_quote(4))
    time.sleep(1)

    clear_screen()
    get_type_and_level()

    print(quotes.get_quote(7))
    time.sleep(2)

    while True:
        win, loss = start_game()
        
        if (win < loss):
            print(f"{quotes.get_quote(9, colors.red)}".replace("%win%", str(win)).replace("%loss%", str(loss)))
        elif (win == loss):
            print(f"{quotes.get_quote(9, colors.yellow)}".replace("%win%", str(win)).replace("%loss%", str(loss)))
        else:
            print(f"{quotes.get_quote(9, colors.green)}".replace("%win%", str(win)).replace("%loss%", str(loss)))

        if (input(quotes.get_question(3)).upper() == "Y"):
            clear_screen()
            get_type_and_level()
        else:
            break

main()