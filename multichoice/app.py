from Question import *

question_prompts = [

    "What is your hobbies?\n(a)Cricket \n(b)Carrom \n(c)BasketBall\n\n",
    "What is your company name? \n(a)Capco \n(b)Societe Generale \n(c)Thomson\n\n",
    "What is your favourite fruit?\n(a)Orange \n(b)Banana \n(c)Apple\n\n"
]

questions = [

    Question(question_prompts[0],"a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
               score += 1

    print("You Got " + str(score) + "/" + str(len(questions)) +  " correct ")

run_test(questions)