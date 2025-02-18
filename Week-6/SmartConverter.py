# Take in a measurement input with following format
# `{number} {unit}`
# Based on the unit, figure out the corresponding 
# conversion:
#   - ml <---> fl_oz
#   - l <---> gal
#   - kg <---> lbs
#   - C <---> F
def main():
    user_measurement = input("Enter your measurement: ")

    # Split the input into the number portion and
    # unit portion
    number = ""
    unit = ""
    user_measurement = user_measurement.replace(" ", "")

    for char in user_measurement:
        if char.isdigit() or char == ".":
            number += char
        else:
            unit += char

    number = float(number)

    # print(f"number portion: {number}")
    # print(f"unit portionl: {unit}")

    converted_number = 0.0
    converted_unit = ""

    match unit:
        case "ml":
            # 1ml == 0.0033814 fl oz
            converted_number = number * 0.033814
            converted_unit = "fl_oz"
        case "fl_oz":
            converted_number = number / 0.033814
            converted_unit = "ml"
        case "l":
            # 1l == 0.264172 gal
            converted_number = number * 0.264172
            converted_unit = "gal"
        case "gal":
            converted_number = number / 0.264172
            converted_unit = "l"
        case "kg":
            # 1kg == 2.20462 lbs
            converted_number = number * 2.20462
            converted_unit = "lbs"
        case "lbs":
            converted_number = number / 2.20462
            converted_unit = "kg"
        case "C":
            # (0°C × 9/5) + 32 = 32°F
            converted_number = (number * 9/5) + 32
            converted_unit = "F"
        case "F":
            # (0°F − 32) × 5/9 = -17.78°C
            converted_number = (number - 32) * 5/9
            converted_unit = "C"
    
    print(f"{number:.2f} {unit} == {converted_number:.2f} {converted_unit}")

    
        

if __name__ == "__main__":
    main()