class quizard:

    def __init__(self, question_type: int, question_level: int):
        self.question_type = question_type
        self.question_level = question_level
    
    def get_question(self):
        
        #addition
        if (self.question_type == 1):
            print("addition")

        #subtraction
        elif (self.question_type == 2):
            print("subtraction")

        #multiplication
        elif (self.question_type == 3):
            print("multiplication")

        #division
        else:
            print("division")