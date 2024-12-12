# Quiz 
import json
import random
import time

def show_progress_bar(current, total, bar_length=20):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {current}/{total} questions', end='')
    print()

with open("questions.json", "r") as f:
    questions = json.load(f)["questions"]

print("Welcome to the Python Quiz! ")
print("Test your knowledge by answering ten Python questions.")
print("Time start now...")
start_time = time.time()
random_questions = random.sample(questions, 10)

score = 0
for i, q in enumerate(random_questions):
    print()
    question = q["question"]
    choices = q["choice"]
    answer = q["answer"]

    print(f"Q{i+1}: {question}")
    random.shuffle(choices)
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
    
    show_progress_bar(i+1, len(random_questions))


end_time = time.time()
tim_taken = round(end_time - start_time, 2)
print()
print(f"Score: {score}/{len(random_questions)} 🎉")
print(f"You took {tim_taken} second to complete the quiz.")