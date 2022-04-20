import numpy as np
from datetime import datetime
import time
from csv import DictWriter


# Code used from: https://codereview.stackexchange.com/questions/263306/python-math-quiz
# Minor tweaks have been added


# TODO:
# - Ensure GIT SDLC
# - creating a csv record for each run
#         - name,time_of_run,score,incorrect_question_list,time_taken
# - Biggie :
#      - bigger numbers
#      - add decimals support
#      - Change 'BAN_NEGATIVE_NUMBERS' to False if name == Biggie
# - Enable app to be run on Chromebook (think Streamlit)
# - Create a webapp for Data Analysis (Streamlit)
# - Port everything to cloud


QUESTIONS = 10
BAN_NEGATIVE_NUMBERS = True
OPERATORS_OLD = ["-", "+", "*", "//"]
OPERATORS_YOUNG = ["-", "+"]
MAX_NUMBER, DECIMALS = 20, 2
MAX_ERROR = 10 ** (1 - DECIMALS)
INCORRECT_QUESTION_LIST = []
RECORD_KEEPING_BOOK = r'./test_data.csv'


def define_operator():
    name = str.casefold(input('Are you Biggie or Chiggie?: '))
    if name == 'biggie':
        return OPERATORS_OLD, name
    elif name == 'chiggie':
        return OPERATORS_YOUNG, name
    else:
        print("No intruders allowed!!! Go away Boba Fett!!! :P\n\n")
        # define_operator()
        # return OPERATORS_YOUNG


def generate_questions(operator=OPERATORS_YOUNG):
    operators = np.random.choice(a=operator, size=(QUESTIONS, 1))
    numbers = np.random.choice(a=MAX_NUMBER, size=(QUESTIONS, 2))
    for operator, (num1, num2) in zip(operators, numbers):
        if num1 < num2 and operator == "-" and BAN_NEGATIVE_NUMBERS and num2 != 0:
            num1, num2 = num2, num1
        yield f"{num1} {operator[0]} {num2}"


def get_guess():
    try:
        return float(input("> "))
    except ValueError:
        print("Ooops, you need to write in a number!")
        return float("Inf")


def append_dict_as_row(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:    # open file in append mode
        dict_writer = DictWriter(write_obj, dict_of_elem, field_names)
        dict_writer.writerow(dict_of_elem)


def quiz(score=0):
    print('*' * 40)
    print(f"\n** Welcome! This is a {QUESTIONS} question quiz! **\n")
    print('*' * 40)
    print()
    operator, name = define_operator()  # gets called only once
    while operator is None:
        operator = define_operator()  # gets called only once
        # operator = OPERATORS_YOUNG
    # print(operator)
    print('\n\nGET READYY...and your time begins ...')
    time.sleep(2)
    print('\n\t\t....NOW!\n')
    start_time = datetime.now()
    incorrect_questions_list = []
    for question in generate_questions(operator):
        print(question)
        guessed_right = abs(get_guess() - eval(question)) <= MAX_ERROR
        score += 1 if guessed_right else 0
        if not guessed_right: # adding incorrect questions to a list
            incorrect_questions_list.append(question)
        print("Correct!" if guessed_right else "Incorrect", "\nScore", score, "\n")
    total_time_taken = datetime.now() - start_time
    print(f"Your score was {score}/{QUESTIONS} = {round(100*score/QUESTIONS, 2)}")
    print(f"\nTime to complete the quiz : {float(total_time_taken.total_seconds())}")
    field_names = ['name', 'time_of_run', 'score', 'incorrect_question_list', 'time_taken']
    dict_of_elem = {'name': name
                    , 'time_of_run': start_time
                    , 'score': (score/QUESTIONS)*100
                    , 'incorrect_questions_list': incorrect_questions_list
                    , 'time_taken': float(total_time_taken.total_seconds())}
    append_dict_as_row('test_data.csv', dict_of_elem, field_names)
    print("Thank you for playing!")


if __name__ == "__main__":
    quiz()
