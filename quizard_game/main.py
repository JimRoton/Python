import os
import time
from datetime import datetime as datetime, timedelta as timedelta
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

def ask_question() -> question:
    qz = quizard()
    q = qz.get_question(quizard.question_type, quizard.question_level)

    q.start_time = datetime.now()
    q.answer = int(input(f"{quotes.get_quote(8)}".replace("%question_statement%", q.get_question_statement())))
    q.end_time = datetime.now()

    return q

def start_game() -> any:
    i = 1
    win = 0
    loss = 0
    total_time = 0

    while (i <= 10):
        clear_screen()

        print (f"Question {i}:")
        q = ask_question()

        if (q.answer == q.get_answer()):
            print(quotes.get_random_success())
            win += 1
        else:
            print(quotes.get_random_failure(q.get_answer(), colors.green))
            loss += 1

        print(f"{quotes.get_quote(12)}".replace("%seconds%", str(q.get_total_time())))
        total_time += q.get_total_time()
    
        i += 1
        time.sleep(3)

    return win, loss, total_time

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
        win, loss, total_time = start_game()
        
        if (win < loss):
            print(f"{quotes.get_quote(9, colors.red)}".replace("%win%", str(win)).replace("%loss%", str(loss)))
        elif (win == loss):
            print(f"{quotes.get_quote(9, colors.yellow)}".replace("%win%", str(win)).replace("%loss%", str(loss)))
        else:
            print(f"{quotes.get_quote(9, colors.green)}".replace("%win%", str(win)).replace("%loss%", str(loss)))

        print(f"{quotes.get_quote(13, colors.green)}".replace("%total_time%", str(total_time)))

        if (input(quotes.get_question(3)).upper() == "Y"):
            clear_screen()
            get_type_and_level()
        else:
            break

q = question(10, 10, 1)
q.start_time = datetime.now()
q.end_time = q.start_time + timedelta(seconds=3661)

s = q.get_mod_seconds()
m = q.get_mod_minutes()
h = q.get_mod_hours()
print(s)
print(m)
print(h)
main()