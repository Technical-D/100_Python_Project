# Quiz 
import json
import random
import time

def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions

def get_randome_questions(questions, num_question):
    if num_question > len(questions):
        num_question = len(questions)
    
    random_questions = random.sample(questions, num_question)

    return random_questions

def show_progress_bar(current, total, bar_length=20):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {current}/{total} questions', end='')
    print()

questions = load_questions()
random_questions = get_randome_questions(questions, 10)
start_time = time.time()
score = 0

print("Welcome to the Python Quiz! ")
print("Test your knowledge by answering ten Python questions.")
print("Time start now...")

for i, q in enumerate(random_questions):
    print()
    question = q["question"]
    choices = q["choice"]
    answer = q["answer"]
    
    random.shuffle(choices)

    print(f"Q{i+1}: {question}")
    for j, choice in enumerate(choices):
        print(f"{j + 1}. {choice}")
    
    while True:
        user_choice_num = input("Enter the number corresponding to your choice (1/2/3/4): ")
        try:
            user_choice_num = int(user_choice_num)
            if user_choice_num <= 0 or user_choice_num > 4:
                print("Inavlid choice. Number out of range!")
                continue
            else:
                break
        except:
            print("Invalid choice!")
    
    if choices[user_choice_num - 1] == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"Correct answer: {answer}")
    
    show_progress_bar(i+1, len(random_questions))


end_time = time.time()
tim_taken = round(end_time - start_time, 2)
print()
print(f"Score: {score}/{len(random_questions)} 🎉")
print(f"You took {tim_taken} second to complete the quiz.")