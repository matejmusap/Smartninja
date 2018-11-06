def main():
    x = float(raw_input("Unesi broj:"))
    y = float(raw_input("Unesi drugi broj:"))
    operator = raw_input("Unesi operaciju(+,-,*,/):")
    print str(calculate(x,y))

def calculate(first_number, second_number, operator):
    try:
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            result = first_number / second_number
        else:
            result = "Write correct operator!"
    except Exception as e:
        result = "Please enter a whole number."
    return result


if __name__ == "__main__":
    main()