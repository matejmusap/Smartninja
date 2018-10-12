x = int(raw_input("Unesi broj:"))
y = int(raw_input("Unesi drugi broj:"))
operation = raw_input("Unesi operaciju(+,-,*,/):")
try:
    if operation == "+":
        print x+y
    elif operation == "-":
        print x-y
    elif operation == "*":
        print x*y
    elif operation == "/":
        print x/y
    else:
    print "Unesi ispravan oprerator!"
except Exception as e:
    print "Please enter a whole number."