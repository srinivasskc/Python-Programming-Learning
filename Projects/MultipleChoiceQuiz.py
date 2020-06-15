# Classes and Objects in Python
from Projects.Question import QuestionClass

question_prompts = [
    "What color are strawberries?\n(a) Green \n(b) Red \n(c) Yellow\n\n",
    "What color are Oranges?\n(a) Green \n(b) Red \n(c) Orange\n\n",
    "What color are Bananas?\n(a) Green \n(b) Orange \n(c) Yellow\n\n"
]

questions = [
    QuestionClass(question_prompts[0], "b"),
    QuestionClass(question_prompts[1], "c"),
    QuestionClass(question_prompts[2], "c")
]


def run_test():
    # global questions
    score = 0
    for Question in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score = score + 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")


run_test()

# Build a Multiple Choice Quiz in Python

# Allow User to take the Quiz
# As User takes the Quiz, we need to track their scores
# At the end, we need to tell how they performed.

# If Stmt, Classes, Loops
