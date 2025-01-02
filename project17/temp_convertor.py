# Temp Convertor
def temp_convertor(temp, convert_from, convert_to):
    if convert_from == 'c':
        if convert_to == 'f':
            return round((temp * 9/5) + 32, 2)
        elif convert_to == 'k':
            return round(temp + 273.15, 2)
    elif convert_from == 'f':
        if convert_to == 'c':
            return round((temp - 32) * 5/9, 2)
        elif convert_to == 'k':
            return round((temp - 32) * 5/9 + 273.15, 2)
    elif convert_from == 'k':
        if convert_to == 'c':
            return round(temp - 273.15, 2)
        elif convert_to == 'f':
            return round((temp - 273.15) * 9/5 + 32, 2)


print("Welcome to Temp convertor!")
print("""
--Units--
C ~ Celsius
F ~ Fahrenheit
K ~ Kelvin
""")
while True:
    temp, unit = input("Enter temperature and unit (e.g., 25 C): ").split()
    try:
        temp = float(temp)
        unit = unit.lower()
        if unit not in ['c', 'f', 'k']:
            print("Invalid temperature unit. Choose from C, F, or K.")
            continue
        break
    except ValueError:
        print("Enter a valid temperature.")

while True:
    convert_to = input("Enter unit to convert to (C/F/K): ").lower()
    
    if convert_to not in ['c', 'f', 'k']:
        print("Invalid conversion unit. Choose from C, F, or K.")
        continue
    
    if unit == convert_to:
        print(f"Conversion unit is the same as input unit ({unit.upper()}).")
        continue
    break

converted_temp = temp_convertor(temp, unit.lower(), convert_to.lower())
print(f"{temp}°{unit.upper()} is equivalent to {converted_temp}°{convert_to.upper()}.")