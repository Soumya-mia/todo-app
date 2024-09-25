import json

with open("questions.json",'r') as file:
    context = file.read()

data = json.loads(context)

for question in data:
    print(question["question_text"])
    for index, alternate in enumerate(question["alternative"]):
        print(f"{index+1}-{alternate}")
    user_choice = int(input("enter a choice:"))
    if user_choice == question["correct_answer"]:
        print("Answer is correct")
    else:
        print("Answer is incorrect")