
class player:

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
