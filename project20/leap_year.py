# Leap year checker
def leap_year_ckecker(year):
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #     else:
    #         return True
    # else:
    #     return False

    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return True
    return False

print("Welcome to Leap Year Checker!")

while True:
    year = input("Enter a year: ")
    try:
        year = int(year)
        break
    except ValueError as e:
        print("Please enter a valid number!")

if leap_year_ckecker(year):
    print(f"Year {year} is a Leap year!")
else:
    print(f"Year {year} is not a Leap year!")