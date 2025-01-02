# BMI(Body Mass Index) Calculator
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_positive_float(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value > 0:
                return value
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

print("Welcome to BMI calculator!\n")

weight = get_positive_float("Enter your weight in kg: ")
height = get_positive_float("Enter your height in meter: ")

bmi = bmi_calculator(weight, height)
print(f"\nYour BMI is: {bmi}")
if bmi < 18.5:
    print("You are Underweight!")
elif 18.5 <= bmi <= 24.9:
    print("You are Normal weight!")
elif 25.0 <= bmi <= 29.9:
    print("You are Overweight!")
elif bmi >= 30.0:
    print('You have obesity!')