# A dictionary that stores questions and answers\
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pair
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed


quiz ={
    "question1": {
        "question": "what is the capital of france?",
        "answer": "paris"
    },
    "question2":{
        "question": "What ud the  capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4":{
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5":{
        "question" : "What is the capital of portugal?",
        "answer": "Lisbon"
    },
    "question6":{
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7":{
        "question": "What is the capital of Austria",
        "answer": "Vienna"
    },
}


score = 0

for key, value in quiz.items():
    print(value['question'])
    answer =input("Answer?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score +1
        print("your score is : " + str(score))
        print("")
        print("")


    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is : " + str(score))
        print("")
        print("")

print("you got " + str(score) + " out of 7 questions correctly")
print("your percentage is " + str(int(score/7 * 100)) + "%")